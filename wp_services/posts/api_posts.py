import allure
from dotenv import load_dotenv
import os
import random
from generator.generator import random_number
from helpers.http_handler import HTTPHandler
from wp_services.posts.models.post_model_del import PostModelDel
from wp_services.posts.models.posts_model import AllPostsModel, PostModel
from wp_services.posts.payloads import Payloads

load_dotenv()


class PostsAPI(HTTPHandler):

    BASE_HOST = f"{os.getenv('WP_BASE_HOST')}/index.php?rest_route=/"
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

    def delete_random_posts(self, list_ids, basic_auth_wp):
        with allure.step("Удалить рандомное число posts"):
            count_posts_to_delete = random.randint(1, len(list_ids))
            posts_to_delete = random.sample(list_ids, count_posts_to_delete)
            deleted_posts = []

            for post_id in posts_to_delete:
                self.delete_post(post_id, basic_auth_wp)
                deleted_posts.append(post_id)

            return deleted_posts

    def delete_remaining_posts(self, new_posts_ids, del_ids, basic_auth_wp):
        with allure.step("Удалить оставшиеся posts которые были созданы для теста"):
            remaining_ids = [post_id for post_id in new_posts_ids if post_id not in del_ids]
            deleted_posts = []

            for post_id in remaining_ids:
                self.delete_post(post_id, basic_auth_wp)
                deleted_posts.append(post_id)

            return deleted_posts

    def re_delete_post(self, post_id, auth):
        with allure.step("Попытаться удалить удаленный пост"):
            response = HTTPHandler.double_delete(
                url=f"{self.posts}/{post_id}&force=true",
                auth=auth
            )

            return response.status_code
