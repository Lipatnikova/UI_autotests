from pydantic import ValidationError
from faker import Faker

from generator.generator import generate_current_date, random_number
from helpers.convert_data import ConversionData
from wp_services.posts.models.posts_model import PayloadCreatePost, PayloadUpdatePost

fake = Faker()


class Payloads:

    @staticmethod
    def generate_post():
        post_data = {
            "title": fake.word(),
            "content": fake.text(),
            "status": "publish",
            "comment_status": "open",
            "ping_status": "open"
        }
        return PayloadCreatePost(**post_data).model_dump()
    try:
        fake_user = generate_post()
    except ValidationError as e:
        print(e)

    @staticmethod
    def update_post():
        post_data = {
            "title": fake.word(),
            "content": fake.text(),
            "comment_status": "open"
        }
        return PayloadUpdatePost(**post_data).model_dump()

    try:
        fake_user = generate_post()
    except ValidationError as e:
        print(e)

    @staticmethod
    def create_post_db():
        post_date = generate_current_date()
        post_modified_gmt = ConversionData.convert_to_gmt(post_date)
        return {
            "post_author": 1,
            "post_name": fake.name(),
            "comment_status": "open",
            "post_date": post_date,
            "post_date_gmt": post_modified_gmt,
            "post_modified": post_date,
            "post_modified_gmt": post_modified_gmt,
            "guid": "http://",
            "post_content": fake.text(),
            "post_title": fake.sentence(),
            "post_excerpt": fake.text(),
            "to_ping": fake.text(),
            "pinged": fake.text(),
            "post_content_filtered": fake.text()
        }

    @staticmethod
    def update_post_db():
        return {
            "post_author": random_number(2, 10),
            "post_name": fake.name(),
            "post_title": fake.sentence(),
            "post_date": generate_current_date(),
            "post_date_gmt": ConversionData.convert_to_gmt(generate_current_date()),
            "post_modified": generate_current_date(),
            "post_modified_gmt": ConversionData.convert_to_gmt(generate_current_date())
        }
