#!/usr/bin/python3
'''A classs Amenity that inherits Basemode'''
from models.base_models import Basemodel


class Amenity(Basemodel):
    '''Amenity information
    Attributes:
        name (str): The name of the amenity.
    '''

    name = ''
