#!/usr/bin/python3
"""
"""

import uuid
from datetime import datetime

class BaseModel:
    def __init__(self, *args, **kwargs):
        formatted_time = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, formatted_time))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()

    def save(self):
        """
        updates updated_at attribute with current date time
        """
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """
        """
        instn_dict = self.__dict__.copy()
        instn_dict["__class__"] = self.__class__.__name__
        instn_dict["created_at"] = self.created_at.isoformat()
        instn_dict["updated_at"] = self.updated_at.isoformat()
        return instn_dict

    def __str__(self):
        """
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

if __name__ == '__main__':
    my_model = BaseModel()
    my_model.name = "My First Model"
    my_model.my_number = 89
    print(my_model)
    my_model.save()
    print(my_model)
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
		
    print("--")
    my_new_model = BaseModel(**my_model_json)
    print(my_new_model.id)
    print(my_new_model)
    print(type(my_new_model.created_at))

    print("--")
    print(my_model is my_new_model)

