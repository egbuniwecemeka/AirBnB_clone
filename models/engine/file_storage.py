import json
import os

class FileStorage:
    """serializes instances to a JSON file and deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the __object dctionary providing access to all stored objects"""
        return FileStorage.__objects
    
    def new(self, obj):
        """sets object in __objects dictionary with key <obj class name>.id"""
        obj_cls_name = obj.__class__.__name__
        key = f"{obj_cls_name}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file at __file_path"""
        all_objs = FileStorage.__objects

        obj_dict = {}

        for obj in all_objs.keys():
            obj_dict[obj] = all_objs[obj].to_dict()
        
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as file:
            json.dump(obj_dict, file)
        
    def reload(self):
        """deserializes JSON file to __objects"""
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as file:
                try:
                    obj_dict = json.load(file)

                    for key, value in obj_dict.items():
                        class_name, obj_id = key.split('.')
                        # get class name dynamically from class_name
                        cls = eval(class_name)
                        instance_val = cls(**value)
                        FileStorage.__objects[key] = instance_val
                except Exception:
                    pass