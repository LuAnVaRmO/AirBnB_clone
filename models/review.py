#!/usr/bin/python3
""" holds class review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Representation of a review """
    place_id = ''
    user_id = ''
    text = ""

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)
