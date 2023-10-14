#!/usr/bin/python3
'''A class place that inherits Basemodel'''
from models.base_model import Basemodel


class Place(Basemodel):
    '''Place information'''

    city_id = ''
    user_id = ''
    name = ''
    description: string = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
