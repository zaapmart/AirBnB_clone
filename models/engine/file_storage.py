import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

# Importing FileNotFoundError here
try:
    FileNotFoundError
except NameError:
    FileNotFoundError = IOError


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, "w") as file:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, "r") as file:
                data = json.load(file)
                for key, value in data.items():
                    cls_name = value['__class__']
                    if cls_name == 'User':
                        cls = User
                    elif cls_name == 'Place':
                        cls = Place
                    elif cls_name == 'State':
                        cls = State
                    elif cls_name == 'City':
                        cls = City
                    elif cls_name == 'Amenity':
                        cls = Amenity
                    elif cls_name == 'Review':
                        cls = Review
                    else:
                        continue
                    self.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass
