#!/usr/bin/python3
""" Module - BaseModel """
import uuid
import models
import datetime
from datetime import datetime


class BaseModel:
    """
    Class BaseModel
    Attributes:
        id (int): universally unique identifier
        created.at (int): Date of creation in ISO format
        updated.at (int): Date of last update
    """

    def __init__(self, *args, **kwargs):
        """Class Constructor"""
        if kwargs:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                if k != '__class__':
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """ print in format: [<class name>] (<self.id>) <self.__dict__> """
        n = __class__.__name__
        return ("[{}] ({}) {}".format(n, self.id, self.__dict__))

    def save(self):
        """ updates attribute updated_at with the current datetime """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary representation """
        our_dict = dict(self.__dict__)
        our_dict['__class__'] = self.__class__.__name__
        our_dict['created_at'] = self.created_at.isoformat()
        our_dict['updated_at'] = self.updated_at.isoformat()
        return our_dict
