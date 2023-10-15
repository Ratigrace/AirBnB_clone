#!/usr/bin/python3
'''A class State that inherits Basemodel'''

from models.base_model import BaseModel


class State(BaseModel):
    '''Provides state information
    Attributes:
        name (str): The name of the state
    '''

    name = ''
