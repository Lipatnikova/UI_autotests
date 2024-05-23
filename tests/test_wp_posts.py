import allure
import pytest

from generator.generator import random_choice
from helpers.assertions import Assertions
from helpers.convert_data import ConversionData, ResponseConverter
from wp_services.posts.api_posts import PostsAPI
from wp_services.posts.db_posts import DbPosts
from wp_services.posts.payloads import Payloads


class TestWordPressPosts:
    api_posts = PostsAPI()
    db_post = DbPosts()

    @pytest.mark.back_autotests
    @allure.epic("Reference WordPress")
    @allure.feature("Работа с Posts")
    @allure.story("Создание Post")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.testcase("D1_1")
    @allure.description("""
    Цель: cоздать post, проверить, что в БД появилась запись соответствующая данным созданного post.
    Предусловие: авторизоваться пользователем Anastasia на сайте WordPress.
    Шаги:
    1. Создать post используя api-запрос и получить ID созданного post.
    2. Найти запись с ID созданного post в БД и получить данные этой записи.
    3. Проверить, что созданный post отображается в списке всех posts БД.
    4. Проверить, что данные полученные из БД и данные сгенерированные при создании post одинаковые. 
    Постусловие: удалить тестовые данные.
    Ожидаемый результат: post создан: имеется запись в БД c данными 
    соответствующими данным введенным при создании post.
    """)
    def test_create_post_and_verify_record_in_db(self, basic_auth_wp):
        post_data = Payloads.generate_post()
        post_id = self.api_posts.create_post(post_data, basic_auth_wp)["id"]
        post_by_id = self.db_post.select_post_by_id(post_id)
        with allure.step("Проверить, что созданный post отображается в списке всех posts БД"):
            assert post_id in self.db_post.select_all_ids_posts(), \
                f"Post with id: {post_id} is not found in DB"
        with allure.step("Проверить, что данные полученные из БД и данные введенные при создании post одинаковые"):
            Assertions.compare_post_data(post_data, post_by_id)

        self.api_posts.delete_post(post_id, basic_auth_wp)

    @pytest.mark.back_autotests
    @allure.epic("Reference WordPress")
    @allure.feature("Работа с Posts")
    @allure.story("Создание и удаление рандомного количества post")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.testcase("D1_2")
    @allure.description("""
    Цель: Создать рандомное количество post, проверить, 
    что в БД количество post изменилось на соответствующее значение.
    Предусловие: авторизоваться пользователем Anastasia на сайте WordPress.
    Шаги:
    1. Получить количество post в БД.
    2. Создать рандомное число post используя api-запросы и получить список всех ID созданных post.
    3. Проверить, что количество post в БД увеличилось на число созданных post.
    4. Удалить рандомное число post (не более числа созданных post по п.2) используя api-запрос и 
    получить список всех ID удаленных post.
    5. Проверить, что количество post в БД уменьшилось на число удаленных post.
    Постусловие: удалить тестовые данные.
    Ожидаемый результат: 
    1. Количество post в БД увеличилось на число созданных post.
    2. Количество post в БД уменьшилось на число удаленных post.
    """)
    def test_create_and_del_random_count_post(self, basic_auth_wp):
        db_posts_before = self.db_post.select_all_ids_posts()
        new_posts_ids = self.api_posts.create_random_posts(basic_auth_wp)
        db_posts_after = self.db_post.select_all_ids_posts()
        with allure.step("Проверить, что количество post в БД увеличилось на число созданных post"):
            Assertions.verify_count_created_posts(db_posts_before, new_posts_ids, db_posts_after)
        del_ids = self.api_posts.delete_random_posts(new_posts_ids, basic_auth_wp)
        db_posts_after_del = self.db_post.select_all_ids_posts()
        with allure.step("Проверить, что количество post в БД уменьшилось на число удаленных post"):
            Assertions.verify_count_deleted_posts(db_posts_after, del_ids, db_posts_after_del)

        self.api_posts.delete_remaining_posts(new_posts_ids, del_ids, basic_auth_wp)

    @pytest.mark.back_autotests
    @allure.epic("Reference WordPress")
    @allure.feature("Работа с Posts")
    @allure.story("Обновление данных Post")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.testcase("D1_3")
    @allure.description("""
    Цель: обновить post, проверить, что в БД изменились данные post на введенные при обновлении данных post.
    Предусловие: авторизоваться пользователем Anastasia на сайте WordPress.
    Шаги:
    1. Создать post используя api-запрос и получить ID созданного post.
    2. Найти запись с ID созданного post в БД и получить данные этой записи.
    3. Обновить созданный post используя api-запрос.
    4. Проверить, что данные созданного поста изменились после его обновления.
    5. Проверить, что данные в БД обновленного поста изменились на данные введенные при обновлении post по п.3.
    Постусловие: удалить тестовые данные
    Ожидаемый результат: post обновлен: имеется запись в БД c данными 
    соответствующими данным введенным при обновлении post.
    """)
    def test_update_post_and_verify_record_in_db(self, basic_auth_wp):
        post_data = Payloads.generate_post()
        post_id = self.api_posts.create_post(post_data, basic_auth_wp)["id"]
        post_db_before = self.db_post.select_post_by_id(post_id)
        post_data_update = Payloads.generate_post()
        self.api_posts.update_post(post_data_update, basic_auth_wp, post_id)
        post_db_after = self.db_post.select_post_by_id(post_id)
        with (allure.step("Проверить, что данные созданного поста изменились после его обновления")):
            assert post_db_before != post_db_after, \
                f"Post with id: {post_id} is not updated"
        with allure.step("Проверить, что данные полученные из БД и данные введенные при обновлении post одинаковые"):
            Assertions.compare_post_data(post_data_update, post_db_after)

        self.api_posts.delete_post(post_id, basic_auth_wp)

    @pytest.mark.back_autotests
    @allure.epic("Reference WordPress")
    @allure.feature("Работа с Posts")
    @allure.story("Удаление Post")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.testcase("D1_4")
    @allure.description("""
    Цель: Удалить post, проверить, что в БД post был удален.
    Предусловие: авторизоваться пользователем Anastasia на сайте WordPress.
    Шаги:
    1. Cоздать рандомное число post и получить список ID всех post используя api-запрос.
    2. Выбрать рандомный post по ID из списка всех post.
    3. Удалить post используя api-запрос.
    4. Проверить, что post с выбранным ID отсутствует в списке post в БД.
    5. Проверить, что информация о post не возвращается при попытке удалить повторно post api-запросом. 
    Ожидаемый результат: 
    1. post с выбранным ID отсутствует в списке post в БД.
    2. Информация о post не возвращается при попытке удалить повторно post.
    """)
    def test_delete_post_and_verify_record_in_db(self, basic_auth_wp):
        posts_ids = self.api_posts.create_random_posts(basic_auth_wp)
        random_post_id = random_choice(posts_ids)
        self.api_posts.delete_post(random_post_id, basic_auth_wp)
        db_all_posts = self.db_post.select_all_ids_posts()
        with allure.step("Проверить, что post с выбранным ID отсутствует в списке post в БД"):
            assert random_post_id not in db_all_posts, \
                f"Post with id: {random_post_id} is not deleted"
        with allure.step("Проверить, что информация о post не возвращается при попытке удалить повторно post"):
            self.api_posts.re_delete_post(random_post_id, basic_auth_wp)

        self.api_posts.delete_remaining_posts(posts_ids, [random_post_id], basic_auth_wp)

    @pytest.mark.back_autotests
    @allure.epic("Reference WordPress")
    @allure.feature("Работа с Posts")
    @allure.story("Создание Post")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.testcase("D2_1")
    @allure.description("""
    Цель: Создать post используя SQL-запрос к БД, проверить, что в списке post имеется созданный post.
    Предусловие: авторизоваться пользователем Anastasia на сайте WordPress.
    Шаги:
    1. Создать post используя SQL-запрос к БД и получить его ID.
    2. Проверить, что созданный post имеет данные введенные при его создании.
    3. Проверить, что в списке всех post имеется созданный post.
    Постусловие: Удалить тестовые данные
    Ожидаемый результат: post создан: имеется запись в БД c данными 
    соответствующими данным введенным при создании post.
    """)
    def test_create_post_in_db_and_verify_post_data(self, basic_auth_wp):
        post_data = Payloads.create_post_db()
        new_post_id = self.db_post.create_post(post_data)
        new_post_data = self.api_posts.get_post_by_id(new_post_id)
        all_posts = self.api_posts.get_all_posts()
        with allure.step("Проверить, что созданный post имеет данные введенные при его создании"):
            Assertions.check_post_data_in_post_data(post_data, new_post_data)
        with ((allure.step("Проверить, что в списке всех post имеется созданный post"))):
            assert new_post_data in all_posts, \
                f"List all post hasn\'t created post with ID {new_post_id}"

        self.db_post.delete_post_by_id(new_post_id)

    @pytest.mark.back_autotests
    @allure.epic("Reference WordPress")
    @allure.feature("Работа с Posts")
    @allure.story("Обновление данных Post")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.testcase("D2_2")
    @allure.description("""
    Цель: обновить post, проверить, что в БД изменились данные post на введенные при обновлении данных post.
    Предусловие: авторизоваться пользователем Anastasia на сайте WordPress.
    Шаги:
    1. Создать post используя SQL-запрос к БД и получить ID созданного post.
    2. Найти запись с ID созданного post в БД и получить данные этой записи.
    3. Обновить созданный post используя SQL-запрос к БД.
    4. Проверить, что данные созданного поста изменились после его обновления.
    5. Проверить, что данные в БД обновленного поста изменились на данные введенные при обновлении post по п.3.
    Постусловие: удалить тестовые данные.
    Ожидаемый результат: post обновлен: имеется запись в БД c данными 
    соответствующими данным введенным при обновлении post.
    """)
    def test_update_post_and_verify_post_data(self, basic_auth_wp):
        post_data = Payloads.create_post_db()
        post_id = self.db_post.create_post(post_data)
        post_data_before = self.api_posts.get_post_by_id(post_id)
        update_data = Payloads.update_post_db()
        query_update_str = ConversionData.convert_dict_to_query_update_str(update_data)
        self.db_post.update_post_by_id(query_update_str, post_id)
        post_data_after = self.api_posts.get_post_by_id(post_id)
        with (allure.step("Проверить, что данные созданного поста изменились после его обновления")):
            assert post_data_before != post_data_after, \
                f"Post with id: {post_id} is not updated"
        with allure.step("Проверить, что созданный post имеет данные введенные при его обновлении"):
            Assertions.check_post_data_in_post_data(update_data, post_data_after)

    @pytest.mark.back_autotests
    @allure.epic("Reference WordPress")
    @allure.feature("Работа с Posts")
    @allure.story("Создание и удаление рандомного количества post")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.testcase("D2_3")
    @allure.description("""
        Цель: Создать рандомное количество post, проверить, 
        что в БД количество post изменилось на соответствующее значение.
        Предусловие: авторизоваться пользователем Anastasia на сайте WordPress.
        Шаги:
        1. Получить количество post api-запросом.
        2. Создать рандомное число post используя SQL-запросы к БД и получить список всех ID созданных post.
        3. Проверить, что количество post увеличилось на число созданных post.
        4. Удалить рандомное число post (не более числа созданных post по п.2) используя SQL-запрос и 
        получить список всех ID удаленных post.
        5. Проверить, что количество post уменьшилось на число удаленных post.
        Постусловие: удалить тестовые данные.
        Ожидаемый результат: 
        1. Количество post увеличилось на число созданных post.
        2. Количество post уменьшилось на число удаленных post.
        """)
    def test_create_and_del_random_count_post_in_db(self, basic_auth_wp):
        posts_before = self.api_posts.get_all_posts()
        ids_posts_before = ResponseConverter.extract_all_ids(posts_before)
        count_new_posts = self.db_post.create_random_posts()
        posts_after = self.api_posts.get_all_posts()
        ids_posts_after = ResponseConverter.extract_all_ids(posts_after)
        new_posts_ids = ConversionData.get_unique_values_from_lists(ids_posts_before, ids_posts_after)
        with allure.step("Проверить, что количество post увеличилось на число созданных post"):
            Assertions.verify_count_created_posts_in_db(ids_posts_before, count_new_posts, ids_posts_after)
        count_del_ids = self.db_post.delete_random_posts(new_posts_ids)
        posts_after_del = self.api_posts.get_all_posts()
        ids_posts_after_del = ResponseConverter.extract_all_ids(posts_after_del)
        with allure.step("Проверить, что количество post в БД уменьшилось на число удаленных post"):
            Assertions.verify_count_deleted_posts_in_db(ids_posts_after, count_del_ids, ids_posts_after_del)

        self.db_post.delete_remaining_posts(new_posts_ids, ids_posts_after_del)
