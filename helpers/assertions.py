from data.enums import StatusCode
from helpers.convert_data import ConversionData, ResponseConverter


class Assertions:
    @staticmethod
    def check_response_is_200(response) -> None:
        """The method to check if the response status code is 200 (OK)"""
        status_code = response.status_code
        assert status_code == StatusCode.OK, \
            f'Response status code is incorrect, actual: {status_code}, expected : {StatusCode.OK}'

    @staticmethod
    def check_response_is_200_or_201(response) -> None:
        """The method to check if the response status code is 200 (OK) or 201 (Created)"""
        status_code = response.status_code
        assert status_code == StatusCode.OK or status_code == StatusCode.CREATED, \
            f'Response status code is incorrect, actual: {status_code}'

    @staticmethod
    def compare_post_data(post_data, post_by_id) -> None:
        """Compares two records and returns True if all corresponding values are equal, False otherwise"""
        converted_post_data = ConversionData.extract_values_from_dict(post_data)
        converted_post_by_id = ResponseConverter.convert_post_by_id(post_by_id)
        assert converted_post_data == converted_post_by_id, \
            (f"The data entered when creating the post does not match the data in the database."
             f"Actual data: {converted_post_by_id}. Expected data: {converted_post_data}")
