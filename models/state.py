#!/usr/bin/python3
""" holds class state"""
from models.base_model import BaseModel


class State(BaseModel):
    """Representation of a state """
    name = ''

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)
