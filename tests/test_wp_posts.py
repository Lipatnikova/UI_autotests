import allure
import pytest

from helpers.assertions import Assertions
from wp_services.posts.api_posts import PostsAPI
from wp_services.posts.db_posts import DbPosts
from wp_services.posts.payloads import Payloads


class TestAuth:
    api_posts = PostsAPI()
    db_post = DbPosts()

    @pytest.mark.back_autotests
    @allure.epic("Reference WordPress")
    @allure.feature("Работа с Posts")
    @allure.story("Создание Post")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.testcase("D1_1")
    @allure.description("""
    Цель: Создать post, проверить, что в БД появилась запись соответствующая данным созданного post.
    Предусловие: авторизоваться пользователем Anastasia на сайте WordPress.
    Шаги:
    1. Создать post используя api-запрос и получить ID созданного post.
    2. Найти запись с ID созданного post в БД и получить данные этой записи.
    3. Проверить, что созданный post отображается в списке всех posts БД.
    4. Проверить, что данные полученные из БД и данные сгенерированные при создании post одинаковые. 
    Постусловие: 
    - Удалить тестовые данные
    Ожидаемый результат: 
    - Post создан: имеется запись в БД c данными соответствующими данным введенным при создании post.
    """)
    def test_create_post_and_verify_record_in_db(self, basic_auth_wp):
        post_data = Payloads.generate_post()
        new_post = self.api_posts.create_post(post_data, basic_auth_wp)
        post_id = new_post["id"]
        post_by_id = self.db_post.select_post_by_id(post_id)
        with allure.step("Проверить, что созданный post отображается в списке всех posts БД"):
            assert post_id in self.db_post.select_all_ids_posts(), \
                f"Post with id: {post_id} is not found in DB"
        with allure.step("Проверить, что данные полученные из БД и данные введенные при создании post одинаковые"):
            Assertions.compare_post_data(post_data, post_by_id)

        self.db_post.delete_post_by_id(post_id)
