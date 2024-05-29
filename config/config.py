import os

from dotenv import load_dotenv


class Config:
    WAIT_TIMEOUT = 15


class WpConfig:
    load_dotenv()
    host = os.getenv("WP_DB_HOST")
    user = os.getenv("WP_DB_USER")
    password = os.getenv("WP_DB_PASSWORD")
    db_name = os.getenv("WP_DB_NAME")
    port = 3306
