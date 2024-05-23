import random
from faker import Faker

from data.data import Person
from datetime import datetime

faker_en = Faker('en_US')
Faker.seed()


def create_person():
    """
    Generates a random Person object with fake data.
    Returns:
        generator: A generator that yields a Person object with randomly generated data.
    """
    first_name = faker_en.first_name()
    last_name = faker_en.last_name()
    phone = faker_en.random_number(digits=10)
    username = faker_en.name()
    email = faker_en.email()
    password = faker_en.password()
    yield Person(first_name, last_name, phone, username, email, password)


def generate_current_date() -> str:
    """Generate current date"""
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return current_date


def random_number(start, end) -> int:
    """Get a random number between the given start and end values"""
    return random.randint(start, end)


def random_choice(data):
    """Get a random choice from the given data"""
    return random.choice(data)


def random_sample(list_data, count):
    """Get """
    return random.sample(list_data, count)
