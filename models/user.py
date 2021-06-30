#!/usr/bin/python3
''' User class '''
from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class User(BaseModel, Base):
    ''' User table in class '''
    __tablename__ = "users"
    username = Column(String(60), nullable=False)
    passwd = Column(String(60), nullable=False)
    name = Column(String(60), nullable=False)
    lastname = Column(String(60), nullable=False)
    email = Column(String(60), nullable=False)
    company = Column(String(60), nullable=False)
    gov_id = Column(String(60), nullable=False)
    # from models.order import Order
    order = relationship("Order", back_populates="user")

    def __init__(self, *args, **kwargs):
        """ Initialize the user with the dicts. """
        super().__init__(*args, **kwargs)
