#!/usr/bin/python3
''' Base model for all the tables '''
from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base
from uuid import uuid4

Base = declarative_base()


class BaseModel:
    ''' Base model to declarate tables '''
    id = Column(String(60), primary_key=True)

    def __init__(self, *args, **kwargs):
        ''' Initialize every table '''
        self.id = str(uuid4())
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """String representation of the BaseModel class"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)
