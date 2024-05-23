from datetime import datetime, timedelta
from typing import List


class ConversionData:
    @staticmethod
    def convert_to_gmt(time_string: str) -> str:
        """Converts a given time (format "%Y-%m-%d %H:%M:%S) string to GMT timezone"""
        current_datetime = datetime.strptime(time_string, "%Y-%m-%d %H:%M:%S")
        gmt_offset = timedelta(hours=3)
        gmt_datetime = current_datetime - gmt_offset
        gmt_time_string = gmt_datetime.strftime("%Y-%m-%d %H:%M:%S")
        return gmt_time_string

    @staticmethod
    def format_date(post_date: str) -> str:
        """Formats the date strings to a common format"""
        return datetime.strptime(post_date, '%Y-%m-%dT%H:%M:%S').strftime('%Y-%m-%d %H:%M:%S')

    @staticmethod
    def extract_values_from_dict(dict_create_post_db: dict) -> str:
        """Extracts the values from a dictionary"""
        values = ', '.join(f'"{value}"' for value in dict_create_post_db.values())
        return values

    @staticmethod
    def extract_keys_from_dict(dict_create_post_db: dict) -> str:
        """Extracts the keys from a dictionary"""
        keys = ', '.join(dict_create_post_db.keys())
        return keys

    @staticmethod
    def convert_dict_to_query_update_str(update_dict: dict) -> str:
        """Converts the update_dict values to an update_data string"""
        update_data = ", ".join([f"{key} = '{value}'" for key, value in update_dict.items()])
        return update_data

    @staticmethod
    def get_unique_values_from_lists(list_ids_1, list_ids_2) -> List:
        """Get the unique values from two lists"""
        new_posts_ids = list(set(list_ids_2) - set(list_ids_1))
        return new_posts_ids


class ResponseConverter:
    @staticmethod
    def extract_to_id_list(db_all_posts) -> List:
        """Extracts the IDs from a list of database posts"""
        id_list = [item['ID'] for item in db_all_posts]
        return id_list

    @staticmethod
    def convert_post_by_id(post_by_id) -> str:
        """Converts post_by_id tuple to a string with values in quotes and removes newline characters"""
        converted_values = ', '.join(f'"{value.strip()}"' for value in post_by_id[0])
        return converted_values

    @staticmethod
    def extract_all_ids(posts) -> List:
        """Gets the list of all ids from the posts list"""
        ids = [post['id'] for post in posts]
        return ids
