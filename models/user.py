#!/usr/bin/python3
'''Class user that inherits "Basemodel"'''

from models.base_model import Basemodel


class User(Basemodel):
    '''User information'''

    email = ''
    password = ''
    first_name = ''
    last_name = ''
