#!/usr/bin/python3
"""
This module contains the Base_model
"""
import uuid
from datetime import datetime


class BaseModel:
	""" Class BaseModel
    Attributes:
        id (int): universally unique identifier
        created.at (int): Date of creation in ISO format
        updated.at (int): Date of last update
    """
	def __init__(self):
		self.id = str(uuid.uuid4())
		self.created_at = datetime.now()
		self.updated_at = datetime.now()

	def __str__(self):
		""" print in format: [<class name>] (<self.id>) <self.__dict__> """
		n = __class__.__name__
		return ("[{}] ({}) {}".format(n, self.id, self.__dict__))

	def save(self): 
		""" updates the public instance attribute updated_at with the current datetime """
		self.updated_at = datetime.now()

	def to_dict(self): 
		""" returns a dictionary containing all keys/values of __dict__ of the instance """
		our_dict = dict(self.__dict__)
		our_dict['__class__'] = self.__class__.__name__
		our_dict['created_at'] = self.created_at.isoformat()
		our_dict['updated_at'] = self.updated_at.isoformat()
		return our_dict
	"""
	[BaseModel] (b6a6e15c-c67d-4312-9a75-9d084935e579) {'my_number': 89, 'name': 
	'Holberton', 'updated_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119434), 
	'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': 
	datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)}

	* by using self.__dict__, only instance attributes set will be returned
	* a key __class__ must be added to this dictionary with the class name of the object
	* created_at and updated_at must be converted to string object in ISO format:
		* format: %Y-%m-%dT%H:%M:%S.%f (ex: 2017-06-14T22:31:03.285259)
		* you can use isoformat() of datetime object
	* This method will be the first piece of the serialization/deserialization process: create
	 a dictionary representation with “simple object type” of our BaseModel
	"""
	'''	
	@property
	def id(self):
		"""int: getter id"""
		return self.__id

	@property
	def created_at(self):
		"""int: getter created_at"""
		return self.__created_at

	@property
	def updated_at(self):
		"""int: getter"""
		return self.__updated_at
	
	@id.setter
	def id(self, value):
		self.__id = value

	@updated_at.setter
	def updated_at(self, value):
		self.__updated_at = value
		
	@created_at.setter
	def created_at(self, value):
		self.__created_at = value
	'''