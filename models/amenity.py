#!/usr/bin/python3
""" Module - Amenity"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class Amenity - inherits BaseModel"""
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)
