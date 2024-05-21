import random

import allure

from generator.generator import random_number
from helpers.http_handler import HTTPHandler
from wp_services.posts.models.post_model_del import PostModelDel
from wp_services.posts.models.posts_model import AllPostsModel, PostModel
from wp_services.posts.payloads import Payloads


class PostsAPI(HTTPHandler):

    BASE_HOST = "http://localhost:8000/index.php?rest_route=/"
    posts = f"{BASE_HOST}wp/v2/posts"

    def get_all_posts(self):
        with allure.step("Получить список всех постов"):
            response = HTTPHandler.get(
                url=self.posts,
                model=AllPostsModel
            )

            return response

    def get_post_by_id(self, post_id):
        with allure.step("Получить информацию поста по его ID"):
            response = HTTPHandler.get(
                url=f"{self.posts}/{post_id}",
                model=PostModel
            )

            return response

    def create_post(self, payload, auth):
        with allure.step("Создать новый пост"):
            response = HTTPHandler.post(
                url=self.posts,
                model=PostModel,
                payload=payload,
                auth=auth
            )

            return response

    def update_post(self, payload, auth, post_id):
        with allure.step("Обновить данные поста"):
            response = HTTPHandler.post(
                url=f"{self.posts}/{post_id}",
                model=PostModel,
                payload=payload,
                auth=auth
            )

            return response

    def delete_post(self, post_id, auth):
        with allure.step("Удалить пост"):
            response = HTTPHandler.delete(
                url=f"{self.posts}/{post_id}&force=true",
                model=PostModelDel,
                auth=auth
            )

            return response

    def create_random_posts(self, basic_auth_wp):
        with allure.step("Создать рандомное число posts"):
            posts_ids = []
            for _ in range(random_number(4, 8)):
                payload = Payloads.generate_post()
                new_post = self.create_post(payload, basic_auth_wp)
                posts_ids.append(new_post["id"])
            return posts_ids
