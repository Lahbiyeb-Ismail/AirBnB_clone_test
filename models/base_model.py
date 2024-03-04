#!/usr/bin/python3

import uuid
from datetime import datetime


class BaseModel:
    """Base class for all models"""

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the created_at and updated_at attributes"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary representation of the model"""
        return {
            **self.__dict__,
            "__class__": self.__class__.__name__,
            "created_at": datetime.isoformat(self.created_at),
            "updated_at": datetime.isoformat(self.updated_at),
        }
