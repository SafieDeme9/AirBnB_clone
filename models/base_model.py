#!/usr/bin/python3

""" Creating class BaseModel that defines all common
    attributes/methods for other classes
"""
import uuid
import datetime


class BaseModel:
    """ Defining the class """
    def __init__(self):
        """ instantiation """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """ Returns [<class name>] (<self.id>) <self.__dict__> """
        return "[{}] ({}) {}"\
               .format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ pdates the public instance attribute updated_at
            with the current datetime
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """ Returns a dictionary containing all keys/values of __dict__
            of the instance:
            by using self.__dict__, only instance attributes set will be
            returned
            a key __class__ must be added to this dictionary with the
            class name of the object
            created_at and updated_at must be converted to string
            object in ISO format (%Y-%m-%dT%H:%M:%S.%f)
        """
        dico = dict(self.__dict__)
        dico['__class__'] = self.__class__.__name__
        dico['created_at'] = self.created_at\
            .isoformat(sep='T', timespec='auto')
        dico['updated_at'] = self.updated_at\
            .isoformat(sep='T', timespec='auto')
        return (dico)
