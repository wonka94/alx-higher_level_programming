#!/usr/bin/python3
"""
This script defines a City class.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """City class

    Attributes:
        __tablename__ (str): The table name of the class
        id (int): The city id of the class
        name (str): The city name of the class

    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
