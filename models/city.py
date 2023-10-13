#!/usr/bin python3
"""The 'city' module

It defines one class, 'City(),
which subclasses the 'BaseModel()' class.'
"""
from models.base_model import BaseModel

class City():
    """A city in the application.
    
    Attribute:
        name
        state_id
    """
    
    name = ""
    state_id = ""