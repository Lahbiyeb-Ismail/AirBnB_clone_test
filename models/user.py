#!/usr/bin/python3

from models.base_model import BaseModel


class User(BaseModel):
    """
    User class handles all application users
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
