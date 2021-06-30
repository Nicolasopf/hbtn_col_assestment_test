#!/usr/bin/python3
''' Orders class '''
from sqlalchemy import Column, String, DateTime, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from datetime import datetime


class Order(BaseModel, Base):
    ''' Table Order for the orders.
    The order-users is a many to one relationship, many orders to one user.
    '''
    __tablename__ = "orders"
    date = Column(DateTime, default=datetime.utcnow)
    total = Column(String(60), nullable=False)
    subtotal = Column(String(60), nullable=False)
    taxes = Column(String(60), nullable=False)
    paid = Column(String(60), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'))
    user = relationship("User", back_populates="order")

    def __init__(self, *args, **kwargs):
        ''' Intialize the order. '''
        super().__init__(*args, **kwargs)
