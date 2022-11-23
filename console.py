#!/usr/bin/python3
"""
Console Module
"""

import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """functionality for HBNB console"""
    prompt = "(hbnb) " if sys.__stdin__.isatty() else ""

