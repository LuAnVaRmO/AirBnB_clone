#!/usr/bin/python3
""" holds class Amenity"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Representation of Amenity """
    name = ''

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)
