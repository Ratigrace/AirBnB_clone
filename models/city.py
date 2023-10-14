#!/usr/bin/python3
'''A class City that inherits Basemodel'''
from models.base_model import Basemodel


class City(Basemodel):
    '''Provides city information
    Attributes:
        state_id (str): The state id
        name (str): The name of the city
    '''

    state_id = ''
    name = ''
