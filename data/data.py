from dataclasses import dataclass


@dataclass
class Person:
    first_name: str = None
    last_name: str = None
    phone: str = None
    username: str = None
    email: str = None
    password: str = None
