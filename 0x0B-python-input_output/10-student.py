#!/usr/bin/python3
"""Student to JSON"""


class Student:
    """Student class definition"""

    def __init__(self, first_name, last_name, age):
        """Constructor initializater"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        ''' Method that returns directory description with filter '''

        if isinstance(attrs, list) and all(isinstance(attr, str)
                                           for attr in attrs):
            res = {}
            for x in attrs:
                if x in self.__dict__:
                    res[x] = self.__dict__[x]
            return res
        return self.__dict__
