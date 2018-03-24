#!/bin/usr/python3
""" Module defines Class State"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Class State that inherits from Base and links to the MySQL table states
    Attributes-
    id- id that represents a column
    name- represents a column of a string
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
