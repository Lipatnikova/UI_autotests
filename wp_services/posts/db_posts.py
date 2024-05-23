import allure
from dotenv import load_dotenv
import os

from generator.generator import random_number, random_sample
from helpers.convert_data import ConversionData, ResponseConverter
from helpers.db_handler import DbHandler
from wp_services.posts.payloads import Payloads

load_dotenv()


class DbPosts:

    @staticmethod
    def select_post_by_id(post_id):
        """Retrieves a single post from the database based on the provided post ID"""
        with allure.step("Получить информацию поста по его ID"):
            query_select_post_by_id = f"""
            SELECT post_title, post_content, post_status, comment_status, ping_status
            FROM wp_posts 
            WHERE ID = 
            """
            connection = DbHandler.connect_to_db()
            if connection:
                try:
                    one_post = DbHandler.execute_sql_query(connection, f"{query_select_post_by_id}{post_id}")

                finally:
                    connection.close()
                return one_post

    @staticmethod
    def select_all_ids_posts():
        """Retrieves all post IDs from the database"""
        with allure.step("Получить список post и список их ID"):
            query_select_all_posts = "SELECT * FROM wp_posts"
            connection = DbHandler.connect_to_db()
            if connection:
                try:
                    all_posts = DbHandler.execute_all_sql_query(connection, query_select_all_posts)

                finally:
                    connection.close()
                return ResponseConverter.extract_to_id_list(all_posts)

    @staticmethod
    def create_post(create_data):
        """Creates a new post in the database using the provided data"""
        with allure.step("Создать post"):
            query_create_post = f"""
            INSERT INTO wp_posts ({ConversionData.extract_keys_from_dict(create_data)}) 
            VALUES ({ConversionData.extract_values_from_dict(create_data)});
            """
            connection = DbHandler.connect_to_db()
            if connection:
                try:
                    cursor = connection.cursor()
                    cursor.execute(query_create_post)

                    last_insert_id = cursor.lastrowid
                    guid = f"{os.getenv('WP_BASE_HOST')}/?p={last_insert_id}"
                    update_query = f'UPDATE wp_posts SET guid = "{guid}" WHERE ID = {last_insert_id}'
                    cursor.execute(update_query)
                    connection.commit()

                    new_post_id = last_insert_id
                finally:
                    connection.close()
                return new_post_id

    def create_random_posts(self):
        """Creates random counts posts in the database using the provided data"""
        with allure.step("Создать рандомное число posts"):
            count_new_posts = random_number(2, 5)
            for _ in range(count_new_posts):
                payload = Payloads.create_post_db()
                self.create_post(payload)
            return count_new_posts

    @staticmethod
    def update_post_by_id(query_update_str, post_id):
        """Updates a specific attribute of a post in the database based on the provided post ID"""
        with allure.step("Обновить данные post по ID"):
            query_update_post_by_id = f"""
            UPDATE wp_posts SET {query_update_str} WHERE ID = {post_id}"""
            connection = DbHandler.connect_to_db()
            if connection:
                try:
                    update_post = DbHandler.execute_sql_query(connection, query_update_post_by_id)
                finally:
                    connection.close()
                return update_post

    @staticmethod
    def delete_post_by_id(post_id):
        """Deletes a post from the database based on the provided post ID"""
        with allure.step("Удалить post по ID"):
            query_delete_post_by_id = f"""DELETE FROM wp_posts WHERE ID = """
            connection = DbHandler.connect_to_db()
            if connection:
                try:
                    DbHandler.execute_sql_query(connection, f"{query_delete_post_by_id}{post_id}")
                finally:
                    connection.close()

    def delete_random_posts(self, list_ids):
        with allure.step("Удалить рандомное число posts"):
            count_posts_to_delete = random_number(1, len(list_ids))
            posts_to_delete = random_sample(list_ids, count_posts_to_delete)

            for post_id in posts_to_delete:
                self.delete_post_by_id(post_id)

            return count_posts_to_delete

    @staticmethod
    def delete_remaining_posts(new_posts_ids, ids_posts_after_del):
        with ((allure.step("Удалить оставшиеся post, которые были созданы для теста"))):
            deleted_posts = ConversionData.get_unique_values_from_lists(new_posts_ids, ids_posts_after_del)
            ids_for_del = ConversionData.get_unique_values_from_lists(new_posts_ids, deleted_posts)
            for post_id in ids_for_del:
                DbPosts.delete_post_by_id(post_id)
