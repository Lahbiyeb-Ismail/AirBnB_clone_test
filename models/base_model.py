import uuid
from datetime import datetime

from models import storage


class BaseModel:

    def __init__(self, *args, **kwargs):
        date_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        value = datetime.strptime(value, date_format)
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        cls_name = self.__class__.__name__
        cls_id = self.id
        cls_dict = self.__dict__
        return "[{}] ({}) {}".format(cls_name, cls_id, cls_dict)

    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary representation of the model"""
        return {
            **self.__dict__,
            "__class__": self.__class__.__name__,
            "created_at": datetime.isoformat(self.created_at),
            "updated_at": datetime.isoformat(self.updated_at),
        }
