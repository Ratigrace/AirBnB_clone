#!/usr/bin/python3

import json
from models.base_model import BaseModel

class FileStorage:
    '''Defining File storage class'''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''Returns the dictionary __objects.'''
        return FileStorage.__objects

    def new(self, obj):
        '''Sets in __objects the obj with key <obj class name>.id.'''
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        '''Serializes __objects to the JSON file (path: __file_path).'''
        data = {}
        for key, value in FileStorage.__objects.items():
            data[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(data, file)

    def reload(self):
        '''Deserializes the JSON file to __objects if it exists.'''
        try:
            with open(FileStorage.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split(".")
                    class_obj = globals()[class_name]
                    obj = class_obj(**value)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass

