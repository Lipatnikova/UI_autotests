import os
import pytest
from dotenv import load_dotenv


@pytest.fixture
def basic_auth_wp():
    """Basic Authentication for WordPress"""
    load_dotenv()
    username = os.getenv("WP_USER_NAME")
    password = os.getenv("WP_PASSWORD")
    auth = (username, password)
    return auth
