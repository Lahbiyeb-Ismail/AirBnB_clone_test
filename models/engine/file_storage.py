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
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(FileStorage.__object, f, indent=4)

    def reload(self):
        with open(FileStorage.__file_path, "a+", encoding="utf-8") as f:
            pass
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            try:
                FileStorage.__object = json.load(f)
            except:
                pass
