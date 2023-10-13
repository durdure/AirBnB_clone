#!/usr/bin/python3
"""The 'amenity' module

It defines one class, 'Amenity(),
which subclasses the 'Basemodel()' class.'
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """An amenity provided by a place/house.

    Attributes:
        name
    """
    
    name = ""
