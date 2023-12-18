#!/usr/bin/python3
"""
This module contains the class definition of a City
and an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class City(Base):
    """
    This class contains attributes:
        id: that represents a column of an auto-generated,
        unique integer, can’t be null and is a primary key
        name: that represents a column of a string with maximum 128
        characters and can’t be null
        state_id: that represents a column of an integer,
        can’t be null and is a foreign key to states.id
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"),
                      primary_key=True, nullable=False)
