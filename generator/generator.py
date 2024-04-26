from data.data import Person
from faker import Faker

faker_en = Faker('en_US')
Faker.seed()


def create_person():
    first_name = faker_en.first_name()
    last_name = faker_en.last_name()
    phone = faker_en.random_number(digits=10)
    username = faker_en.name()
    email = faker_en.email()
    password = faker_en.password()
    yield Person(first_name, last_name, phone, username, email, password)
