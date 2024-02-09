#!/usr/bin/python
"""
Module Representing the City Class
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    Class representing a city
    Attributes: state_id and name
    """
    state_id = ""
    name = ""
