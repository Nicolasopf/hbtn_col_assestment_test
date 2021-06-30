#!/usr/bin/python3
''' Initialize the DB storage. '''
from sqlalchemy import create_engine, Column, String, DateTime, Integer
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base
from models.user import User
from models.order import Order
from datetime import datetime
from os import getenv


class DBStorage:
    """interacts with the MySQL database"""
    __engine = None
    __session = None
    classes = ['User', 'Order', 'Shipping', 'Payment']

    def __init__(self):
        """Instantiate a DBStorage object"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format('hbtn_col',
                                             'hbtn_col_pwd',
                                             'localhost',
                                             'hbtn_col_db'))
        self.reload()

    def all(self, cls=None):
        ''' Return a dictionary with all the objects. '''
        new_dict = {}
        for table in classes:
            if cls is None or cls is table:
                objs = self.__session.query(table).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return new_dict

    def save(self):
        ''' save the current session. '''
        self.__session.commit()

    def add(self, obj):
        ''' Adds a new object to '''
        self.__session.add(obj)
        self.save()

    def delete(self, obj=None):
        ''' Deletes an object in the database '''
        if obj:
            self.__session.delete(obj)

    def reload(self):
        ''' Reload the data from the DB. '''
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        ''' Close the session. '''
        self.__session.remove()

    def get(self, cls, id):
        ''' Return the object based on classname and id. '''
        if cls not in classes:
            return None

        all_cls = self.all(cls)
        for obj in all_cls.values():
            if (obj.id == id):
                return obj
        return None


if __name__ == "__main__":
    db = DBStorage()
