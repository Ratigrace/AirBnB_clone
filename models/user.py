#!/usr/bin/python3
'''Class user that inherits "Basemodel"'''

from models.base_model import Basemodel


class User(Basemodel):
    '''User information
    Attributes:
        email (str): The email of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user
    '''

    email = ''
    password = ''
    first_name = ''
    last_name = ''
