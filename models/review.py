#!/usr/bin/python3
""" Module - Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ Class Review - inherits BaseModel """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)
