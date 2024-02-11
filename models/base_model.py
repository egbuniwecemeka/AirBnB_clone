#!/usr/bin/python3
""" The BaseModel class """
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
        A BaseModel class that defines all common
        attributes/methods for other classes:

        Attribute:
        id(string) - assigns a uuid whenever an instance is created
        created_at(datetime) - assigns the current datetime when an instance
        is created
        updated_at(datetime) - assigns the current datetime when an instance
        is created and updated when its object is changed
    """
    def __init__(self, *args, **kwargs):
        """ Initializing BaseModel class

            Args:
            *args() - Unused
            **kwargs - Key/Value pairs of
        """
        tformat = "%Y%m%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for i, j in kwargs.items():
                if i == "creaated_at" or i == "updated_at":
                    self.__dict__[i] = strptime(j, tformat)
                else:
                    self.__dict__[i] = j
        else:
            models.storage.new(self)

    def save(self):
        """ Updates updated_at attribute with current datetime """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """ Returns a dictionary of key/value pairs of __dict__ instance
            self.__dict__ should return set instances attributes
            __class__ is a key class representing the class object
            created_at and updated_at must be converted to string
            object in ISO format
            format: "%Y-%m-%dT%H:%M:%S.%f"
        """
        bcdict = self.__dict__.copy()
        bcdict["class"] = self.__class__.__name__
        bcdict["created_at"] = self.created_at.isoformat()
        bcdict["updated_at"] = self.updated_at.isoformat()
        return bcdict

    def __str__(self):
        """ returns/prints str representation of BaseModel instance
            ex: [<class name>] (<self.id>) <self.__dict__>
        """
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
