import allure

from generator.generator import random_number, random_sample
from helpers.convert_data import ConversionData, ResponseConverter
from helpers.db_handler import DbHandler
from wp_services.posts.payloads import Payloads


class DbPosts:
    db_handler = DbHandler()

    def select_post_by_id(self, db_connection, post_id):
        """Retrieves a single post from the database based on the provided post ID"""
        with allure.step("Получить информацию поста по его ID"):
            query_select_post_by_id = f"""
            SELECT post_title, post_content, post_status, comment_status, ping_status
            FROM wp_posts 
            WHERE ID = 
            """
            one_post = self.db_handler.execute_sql_query(db_connection, f"{query_select_post_by_id}{post_id}")
            return one_post

    def select_all_ids_posts(self, db_connection):
        """Retrieves all post IDs from the database"""
        with allure.step("Получить список post и список их ID"):
            query_select_all_posts = "SELECT * FROM wp_posts"
            all_posts = self.db_handler.execute_all_sql_query(db_connection, query_select_all_posts)
            return ResponseConverter.extract_to_id_list(all_posts)

    def create_post(self, db_connection, create_data):
        """Creates a new post in the database using the provided data"""
        with allure.step("Создать post"):
            query_create_post = f"""
            INSERT INTO wp_posts ({ConversionData.extract_keys_from_dict(create_data)}) 
            VALUES ({ConversionData.extract_values_from_dict(create_data)});
            """
            new_post = self.db_handler.execute_sql_query_create_post(db_connection, query_create_post, create_data)
            return new_post

    def create_random_posts(self, db_connection):
        """Creates random counts posts in the database using the provided data"""
        with allure.step("Создать рандомное число posts"):
            count_new_posts = random_number(2, 5)
            for _ in range(count_new_posts):
                payload = Payloads.create_post_db()
                self.create_post(db_connection, payload)
            return count_new_posts

    def update_post_by_id(self, db_connection, query_update_str, post_id):
        """Updates a specific attribute of a post in the database based on the provided post ID"""
        with allure.step("Обновить данные post по ID"):
            query_update_post_by_id = f"""
            UPDATE wp_posts SET {query_update_str} WHERE ID = {post_id}"""
            update_post = self.db_handler.execute_sql_query(db_connection, query_update_post_by_id)
            return update_post

    def delete_post_by_id(self, db_connection, post_id):
        """Deletes a post from the database based on the provided post ID"""
        with allure.step("Удалить post по ID"):
            query_delete_post_by_id = f"""DELETE FROM wp_posts WHERE ID = """
            self.db_handler.execute_sql_query(db_connection, f"{query_delete_post_by_id}{post_id}")

    def delete_random_posts(self, db_connection, list_ids):
        with allure.step("Удалить рандомное число posts"):
            count_posts_to_delete = random_number(1, len(list_ids))
            posts_to_delete = random_sample(list_ids, count_posts_to_delete)

            for post_id in posts_to_delete:
                self.delete_post_by_id(db_connection, post_id)

            return count_posts_to_delete
