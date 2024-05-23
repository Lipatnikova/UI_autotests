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
    def check_response_is_404(response) -> None:
        """The method to check if the response status code is 404 (Not found)"""
        status_code = response.status_code
        assert status_code == StatusCode.OK or status_code == StatusCode.NOT_FOUND, \
            f'Response status code is incorrect, actual: {status_code}'

    @staticmethod
    def compare_post_data(post_data, post_by_id) -> None:
        """Compares two records and returns True if all corresponding values are equal, False otherwise"""
        converted_post_data = ConversionData.extract_values_from_dict(post_data)
        converted_post_by_id = ResponseConverter.convert_post_by_id(post_by_id)
        assert converted_post_data == converted_post_by_id, \
            (f"The data entered when creating the post does not match the data in the database."
             f"Actual data: {converted_post_by_id}. Expected data: {converted_post_data}")

    @staticmethod
    def verify_count_created_posts(posts_before, new_posts_ids, posts_after) -> None:
        """Verifies the count of created posts"""
        assert len(posts_before) + len(new_posts_ids) == len(posts_after), \
            f"The count of created posts does not match the number of posts in the database. " \
            f"Expected: {len(posts_before) + len(new_posts_ids)}, actual: {len(posts_after)}"

    @staticmethod
    def verify_count_deleted_posts(posts_before, posts_ids, posts_after) -> None:
        """Verifies the count of deleted posts"""
        assert len(posts_before) - len(posts_ids) == len(posts_after), \
            f"The count of deleted posts does not match the number of posts in the database. " \
            f"Expected: {len(posts_before) - len(posts_ids)}, actual: {len(posts_after)}"

    @staticmethod
    def check_post_data_in_post_data(post_data, new_post_data):
        """Checks if the post_data is contained in new_post_data"""
        assert ('post_author' in post_data and 'author' in new_post_data and
                post_data['post_author'] == new_post_data['author']), \
            f"post_author: {post_data.get('post_author')} does not match author: {new_post_data.get('author')}"
        assert ('post_date' in post_data and 'date' in new_post_data and post_data['post_date'] ==
                ConversionData.format_date(new_post_data['date'])), \
            f"post_date: {post_data.get('post_date')} does not match date: {new_post_data.get('date')}"
        assert ('post_name' in post_data and 'slug' in new_post_data and
                post_data['post_name'] == new_post_data['slug']), \
            f"post_name: {post_data.get('post_name')} does not match slug: {new_post_data.get('slug')}"
        assert 'post_title' in post_data and 'title' in new_post_data and post_data['post_title'] == \
               new_post_data['title']['rendered'], \
            (f"post_title: {post_data.get('post_title')} "
             f"does not match title: {new_post_data.get('content', {}).get('rendered')}")

    @staticmethod
    def verify_count_created_posts_in_db(ids_posts_before, count_new_posts, ids_posts_after) -> None:
        """Verifies the count of created posts"""
        assert len(ids_posts_before) + count_new_posts == len(ids_posts_after), \
            f"The count of created posts does not match the number of posts in the database. " \
            f"Expected: {len(ids_posts_before) + count_new_posts}, actual: {len(ids_posts_after)}"

    @staticmethod
    def verify_count_deleted_posts_in_db(ids_posts_after, count_del_ids, ids_posts_after_del) -> None:
        """Verifies the count of deleted posts"""
        assert len(ids_posts_after) - count_del_ids == len(ids_posts_after_del), \
            f"The count of deleted posts does not match the number of posts in the database. " \
            f"Expected: {len(ids_posts_after) - count_del_ids}, actual: {len(ids_posts_after_del)}"
