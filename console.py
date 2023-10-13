#!/usr/bin/python3
"""The Module: 'comsole.py'

Attribute:

"""
import re
import cmd
import json
from models import storage
from models.base_model import BaseModel
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from user import User

current_classes = {'BaseModel': BaseModel, 'User': User,
                   'Amenity': Amenity, 'City': City, 'State': State,
                   'place': Place, 'Review': Review}


class HBNBCommand(cmd.Cmd):
    """The command interpreter.
    

    This class represents the command interperter, and the control center
    of this project. It defines function handlers for all commands inputted
    in the console adn calls the appropriate storage engine APIs to manipulate
    application data / models.

    It sub-classes python's 'cmd.Cmd' class which provides a simples framework
    for writing line-oriented command interpreters.
    """

