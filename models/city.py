#!/usr/bin/python3
""" holds class city"""
from models.base_model import BaseModel


class City(BaseModel):
    """Representation of a city """
    name = ''
    state_id = ''

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)
