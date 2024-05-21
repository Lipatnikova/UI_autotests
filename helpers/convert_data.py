from datetime import datetime, timedelta
from typing import List


class ConversionData:
    @staticmethod
    def convert_to_gmt(time_string) -> str:
        """Converts a given time (format "%Y-%m-%d %H:%M:%S) string to GMT timezone"""
        current_datetime = datetime.strptime(time_string, "%Y-%m-%d %H:%M:%S")
        gmt_offset = timedelta(hours=3)
        gmt_datetime = current_datetime - gmt_offset
        gmt_time_string = gmt_datetime.strftime("%Y-%m-%d %H:%M:%S")
        return gmt_time_string

    @staticmethod
    def extract_values_from_dict(dict_create_post_db):
        """Extracts the values from a dictionary"""
        values = ', '.join(f'"{value}"' for value in dict_create_post_db.values())
        return values

    @staticmethod
    def extract_keys_from_dict(dict_create_post_db) -> str:
        """Extracts the keys from a dictionary"""
        keys = ', '.join(dict_create_post_db.keys())
        return keys


class ResponseConverter:
    @staticmethod
    def extract_to_id_list(db_all_posts) -> List:
        """Extracts the IDs from a list of database posts"""
        id_list = [item['ID'] for item in db_all_posts]
        return id_list

    @staticmethod
    def convert_post_by_id(post_by_id):
        """Converts post_by_id tuple to a string with values in quotes and removes newline characters"""
        converted_values = ', '.join(f'"{value.strip()}"' for value in post_by_id[0])
        return converted_values
