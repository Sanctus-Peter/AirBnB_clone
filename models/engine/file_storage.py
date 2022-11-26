#!/usr/bin/python3
"""Contains the file storage class model"""

import json


class FileStorage:
    """
       serializes instances to a JSON file and
       deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the `obj` with key <obj class name>.id
        """
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """
        Serialize __objects to the JSON file
        """
        with open(self.__file_path, mode="w") as f:
            dict_storage = {}
            for key, value in self.__objects.items():
                dict_storage[key] = value.to_dict()
            json.dump(dict_storage, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        -> Only IF it exists!
        """
        try:
            with open(self.__file_path, 'r') as f:
                jo = json.load(f)
            for key in jo:
                pass
                #self.__objects[key] = classes[jo[key]["__class__"]](**jo[key])
        except FileNotFoundError:
            pass
