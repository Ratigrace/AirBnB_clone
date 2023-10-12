#!/usr/bin/python3
'''Import the FileStorage class from file_storage.py'''

from models.engine.file_storage import FileStorage

'''Create the storage variable as an instance of FileStorage'''
storage = FileStorage()

'''Calling the reload() method on the storage instance'''
storage.reload()
