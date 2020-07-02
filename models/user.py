#!/usr/bin/python3
""" Module - User """
from models.base_model import BaseModel


class User(BaseModel):
    """Class User - inherits BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Constructor"""
        super().__init__(*args, **kwargs)
