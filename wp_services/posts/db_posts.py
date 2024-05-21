import allure

from helpers.convert_data import ConversionData, ResponseConverter
from helpers.db_handler import DbHandler


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
                    new_post = DbHandler.execute_sql_query(connection, query_create_post)
                finally:
                    connection.close()
                return new_post

    @staticmethod
    def update_post_by_id(attribute, value, post_id):
        """Updates a specific attribute of a post in the database based on the provided post ID"""
        with allure.step("Обновить данные post по ID"):
            query_update_post_by_id = f"""
            UPDATE wp_posts SET {attribute} = "{value}" WHERE ID = {post_id};
            """
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
