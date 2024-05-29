import os
import allure
import pytest
from dotenv import load_dotenv
from config.config import WpConfig as Wp
from helpers.convert_data import ConversionData
from helpers.db_handler import DbHandler
from wp_services.posts.api_posts import PostsAPI
from wp_services.posts.models.post_model_del import PostModelDel
from helpers.http_handler import HTTPHandler


@pytest.fixture
def basic_auth_wp():
    """Basic Authentication for WordPress"""
    load_dotenv()
    username = os.getenv("WP_USER_NAME")
    password = os.getenv("WP_PASSWORD")
    auth = (username, password)
    return auth


@pytest.fixture
def http_handler():
    return HTTPHandler()


@pytest.fixture
def posts_url():
    return PostsAPI.posts


@pytest.fixture
def post_model_del():
    return PostModelDel


@pytest.fixture
def delete_post_fixture(http_handler, posts_url, post_model_del):
    with allure.step("Удалить тестовые данные"):
        def delete_post(post_id, auth):
            """Delete post by ID"""
            http_handler.delete(
                url=f"{posts_url}/{post_id}&force=true",
                model=post_model_del,
                auth=auth
            )

    yield delete_post


@pytest.fixture
def delete_remaining_posts(delete_post_fixture):
    with allure.step("Удалить тестовые данные"):
        def delete_posts(new_posts_ids, del_ids, auth):
            """Delete list posts"""
            remaining_ids = [post_id for post_id in new_posts_ids if post_id not in del_ids]

            for post_id in remaining_ids:
                delete_post_fixture(post_id, auth)

    yield delete_posts


@pytest.fixture(scope='session')
def db_connection():
    host = Wp.host
    user = Wp.user
    password = Wp.password
    db = Wp.db_name
    port = Wp.port

    connection = DbHandler.connect_to_db(host, user, password, db, port)
    yield connection
    connection.close()


@pytest.fixture
def db_handler():
    return DbHandler()


@pytest.fixture
def delete_post_by_id(db_handler):
    with allure.step("Удалить тестовые данные"):
        def delete_post(db_connection, post_id):
            """Deletes a post from the database based on the provided post ID"""
            query_delete_post_by_id = f"""DELETE FROM wp_posts WHERE ID = """
            db_handler.execute_sql_query(db_connection, f"{query_delete_post_by_id}{post_id}")

    yield delete_post


@pytest.fixture
def delete_remaining_posts_db(delete_post_by_id):
    with allure.step("Удалить тестовые данные"):
        def delete_posts(db_connection, new_posts_ids, ids_posts_after_del):
            """Delete list posts from db"""
            deleted_posts = ConversionData.get_unique_values_from_lists(new_posts_ids, ids_posts_after_del)
            ids_for_del = ConversionData.get_unique_values_from_lists(new_posts_ids, deleted_posts)
            for post_id in ids_for_del:
                delete_post_by_id(db_connection, post_id)

    yield delete_posts
