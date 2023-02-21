#!/usr/bin/python3
"""
    Define class FileStorage
"""
import json
import models


class FileStorage:
    """Class that serializes instances to a JSON file and deserializes
        JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
            return the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        '''
            set in __objects the obj with key <obj class name>.id
        '''
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        dict_val = obj.to_dict()
        FileStorage.__objects[key] = dict_val

    def save(self):
        """
            serializes __objects to the JSON file (path: __file_path)
        """
        with open(FileStorage.__file_path, 'w', encoding="UTF8") as fl:
            json.dump(FileStorage.__objects, fl)

    def reload(self):
        """
            deserializes the JSON file to __objects (only if the JSON file
            (__file_path) exists; otherwise, do nothing. If the file doesn’t
            exist, no exception should be raised
        """
        try:
            with open(FileStorage.__file_path, encoding="UTF8") as fl:
                FileStorage.__objects = json.load(fl)
            for key, val in FileStorage.__objects.items():
                class_name = val["__class__"]
                class_name = models.classes[class_name]
                FileStorage.__objects[key] = class_name(**val)
        except Exception as excpst:
            pass
