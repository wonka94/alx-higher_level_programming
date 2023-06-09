#!/usr/bin/python3
""" `Student` class module"""


class Student:
    """Represents a Student class"""

    def __init__(self, first_name, last_name, age):
        """Sets attributes of a new Student instance

            Args:
                first_name (str): The first name
                last_name (str): The last name
                age (int): The age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns the dictionary description with simple
           data structure for JSON serialization of Student
        """
        desc = {}

        if attrs is not None:
            keys = [key for key in self.__dict__ if key in attrs]
        else:
            keys = [key for key in self.__dict__]

        for key in keys:
            value = getattr(self, key)
            if type(value) in [list, dict, str, int, bool]:
                desc[key] = value

        return desc

    def reload_from_json(self, json):
        """ Replaces all attributes of the Student instance """
        for key in json:
            setattr(self, key, json[key])
