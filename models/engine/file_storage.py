#!/usr/bin/python3
""" Module to store data on JSON Format. """
import json


class FileStorage:
    """ Class filestorage """
    def __init__(self, file_path="file.json", objects={}):
        self.__file_path = file_path
        self.__objects = objects
        #reload()
    def all(self):
        """ Return the dict __objects """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key=<obj class name>.id """
        if obj:
            key = "{}.{}".format(self.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """ serializes __objetcs to the JSON file (path: __file_path) """

    def reload(self):
        """ Deserializes the JSON file to __objects """
