#!/usr/bin/python3

from models import storage
import uuid
from datetime import datetime


class BaseModel:
    '''defining the BaseModel class'''

    def __init__(self, *args, **kwargs):
        '''Initializing public instance attributes.
        Args:
            *args: unused
            **kwargs: (dict) of attributes
        '''

        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

            '''Call the new method of storage for new instances'''
            storage.new(self)

    def __str__(self):
        '''returns a string representation of BaseModel'''
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        '''updates current attributes with date and time'''
        self.updated_at = datetime.now()
        '''Calling the save method of storage to save the instance'''
        storage.save()

    def to_dict(self):
        '''returns a dictionary containg keys/values for instances'''
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

