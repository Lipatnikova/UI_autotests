import pymysql
from config.config import WpConfig as Wp


class DbHandler:
    @staticmethod
    def connect_to_db():
        """This method establishes a connection to the database using
        the provided parameters and returns the connection object"""
        try:
            connection = pymysql.connect(
                host=Wp.host,
                user=Wp.user,
                password=Wp.password,
                db=Wp.db_name,
                charset='utf8',
                port=Wp.port
            )
            return connection
        except Exception as ex:
            print("Connection refused ...")
            print(ex)

    @staticmethod
    def execute_sql_query(connection, query):
        """This method executes an SQL query using the provided database
        connection and returns the result as a list of dictionaries"""
        try:
            with connection.cursor() as cur:
                cur.execute(query)
                result = cur.fetchall()
                connection.commit()
        except Exception as ex:
            print("Error while executing SQL query:")
            print(ex)
            result = None
        return result

    @staticmethod
    def execute_all_sql_query(connection, query):
        """This method executes an SQL query and converts the retrieved
        values from the database into a list of dictionaries"""
        try:
            with connection.cursor() as cur:
                cur.execute(query)
                result = [dict(zip([column[0] for column in cur.description], row)) for row in cur.fetchall()]
                connection.commit()
        except Exception as ex:
            print("Error while executing SQL query:")
            print(ex)
            result = None
        return result
