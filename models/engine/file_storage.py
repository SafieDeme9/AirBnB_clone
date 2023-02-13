#!/usr/bin/python3
import json


from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        """
            set in __objects the obj with key <obj class name>.id
        """
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
        except Exception as excpt:
            pass
