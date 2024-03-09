import json


class FileStorage:

    __file_path = "file.json"
    __object = {}

    def all(self):
        return FileStorage.__object

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__object[key] = obj.to_dict()

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        obj_dict = {
            obj_id: obj.to_dict() for obj_id, obj in FileStorage.__objects.items()
        }
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, "r") as f:
                objs = json.load(f)
                for obj_id, obj_dict in objs.items():
                    cls_name = obj_dict["__class__"]
                    cls = globals()[cls_name]
                    FileStorage.__objects[obj_id] = cls(**obj_dict)
        except FileNotFoundError:
            pass
