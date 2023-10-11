#!/usr/bin/python3

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

    def __str__(self):
        '''returns a string representation of BaseModel'''
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        '''updates current attributes with date and time'''

        self.updated_at = datetime.now()

    def to_dict(self):
        '''returns a dictionary containg keys/values for instances'''
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

        if obj_dict['__class__'] == 'BaseModel':
            ''' Check if "__class__" is "BaseModel"'''
            obj_dict.pop('__class__', None)
            '''Remove the '__class__' key from the dictionary'''

            obj_dict['created_at'] = datetime.strptime(obj_dict['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
            obj_dict['updated_at'] = datetime.strptime(obj_dict['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")
            '''Convert 'created_at' and 'updated_at' strings to datetime objects'''

            instance = BaseModel(**obj_dict)
            '''Create an instance of the BaseModel class using **kwargs'''

        else:
            print("Invalid '__class__' value in the dictionary.")
            '''Handle the case when "__class__" is not "BaseModel"'''

