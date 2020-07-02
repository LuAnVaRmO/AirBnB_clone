#!/usr/bin/python3
""" Module -City"""
from models.base_model import BaseModel


class City(BaseModel):
    """ Class City - inherits BaseModel """
    name = None
    state_id = None

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)
