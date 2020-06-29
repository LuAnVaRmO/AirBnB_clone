#!/usr/bin/python3
""" Module to store data on JSON Format. """
import json
from models.base_model import BaseModel


class FileStorage:
    """ Class filestorage """
    def __init__(self, file_path="file.json", objects={}):
        self.__file_path = file_path
        self.__objects = objects

    def all(self):
        """ Return the dict __objects """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key=<obj class name>.id """
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """ serializes __objetcs to the JSON file (path: __file_path) """
        my_obj = {}
        for k, v in self.__objects.items():
            my_obj[k] = v.to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(my_obj, f)

    def reload(self):
        """ Deserializes the JSON file to __objects """
        try:
            with open(self.__file_path, "r") as f:
                item = json.load(f)
            for k in item:
                self.__objects[k] = BaseModel(**item[k])
        except:
            pass
