#!/usr/bin/python3
""" Module - State"""
from models.base_model import BaseModel


class State(BaseModel):
    """ Class State - inherits BaseModel """
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)
