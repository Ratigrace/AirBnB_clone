#!/usr/bin/python3
'''A class review that inherits Basemodel'''
from models.base_model import BaseModel


class Review(BaseModel):
    '''Review information
    Attributes:
        place_id (str): The Place id.
        user_id (str): The User id.
        text (str): The text of the review.
    '''

    place_id = ''
    user_id = ''
    text = ''
