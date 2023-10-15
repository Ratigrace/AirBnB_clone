#!/usr/bin/python3
'''A classs Amenity that inherits Basemode'''
from models.base_model import BaseModel


class Amenity(BaseModel):
    '''Amenity information
    Attributes:
        name (str): The name of the amenity.
    '''

    name = ''
