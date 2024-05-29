import os
import pymysql


class DbHandler:
    @staticmethod
    def connect_to_db(host, user, password, db, port):
        """This method establishes a connection to the database using
        the provided parameters and returns the connection object"""
        try:
            connection = pymysql.connect(
                host=host,
                user=user,
                password=password,
                db=db,
                charset='utf8',
                port=port
            )
            return connection
        except Exception as ex:
            print("Connection refused ...")
            print(ex)

    @staticmethod
    def handle_error(ex, connection):
        """This method handles the error while executing an SQL query"""
        print("Error while executing SQL query:")
        print(ex)
        connection.rollback()

    def execute_sql_query(self, connection, query):
        """This method executes an SQL query using the provided database
        connection and returns the result as a list of dictionaries"""
        try:
            with connection.cursor() as cur:
                cur.execute(query)
                result = cur.fetchall()
                connection.commit()
        except Exception as ex:
            self.handle_error(ex, connection)
            result = None
        return result

    def execute_all_sql_query(self, connection, query):
        """This method executes an SQL query and converts the retrieved
        values from the database into a list of dictionaries"""
        try:
            with connection.cursor() as cur:
                cur.execute(query)
                result = [dict(zip([column[0] for column in cur.description], row)) for row in cur.fetchall()]
                connection.commit()
        except Exception as ex:
            self.handle_error(ex, connection)
            result = None
        return result

    def execute_sql_query_create_post(self, connection, query, create_data):
        """This method executes an SQL query to create a new post in the database using the provided data"""
        try:
            with connection.cursor() as cur:
                cur.execute(query, create_data)
                last_insert_id = cur.lastrowid
                guid = f"{os.getenv('WP_BASE_HOST')}/?p={last_insert_id}"
                update_query = f'UPDATE wp_posts SET guid = "{guid}" WHERE ID = {last_insert_id}'
                cur.execute(update_query)
                connection.commit()
                new_post_id = last_insert_id
        except Exception as ex:
            self.handle_error(ex, connection)
            new_post_id = None
        return new_post_id
