#!/usr/bin/python
"""
Module for the user class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User class holding user information
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""    
