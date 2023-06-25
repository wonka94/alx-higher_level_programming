#!/usr/bin/python3
""" Base model """


import json
import csv
import os
import turtle


class Base:
    """
    Base class for all models.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes the class.

        Args:
            id (int): The id of the object. If None,
            set id to the current number of objects + 1.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: The JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): A list of objects.
        """
        filename = cls.__name__ + ".json"
        if list_objs is None or len(list_objs) == 0:
            with open(filename, "w") as f:
                f.write("[]")
        else:
            with open(filename, "w") as f:
                list_dicts = list(map(lambda x: x.to_dictionary(), list_objs))
                json_string = cls.to_json_string(list_dicts)
                f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation json_string.

        Args:
            json_string (str): A JSON string.

        Returns:
            list: The list of the JSON string representation json_string.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set.

        Args:
            **dictionary: A dictionary containing key-value
                          pairs for setting attributes.

        Returns:
            object: An instance with all attributes already set.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Writes a list of objects to a CSV file.

        Args:
            cls: The class of the objects.
            list_objs: A list of objects to be serialized.

        Raises:
            TypeError: If list_objs is not a list or contains
            objects of different classes.
        """
        filename = cls.__name__ + ".csv"

        if not list_objs:
            with open(filename, "w") as fi:
                cfile.write("[]")
        else:
            if not all(isinstance(obj, cls) for obj in list_objs):
                raise TypeError("All objects must be of class {}".
                                format(cls.__name__))

            with open(filename, "w") as fi:
                writer = csv.writer(fi)
                for obj in list_objs:
                    if cls.__name__ == "Rectangle":
                        attrs = [obj.id, obj.width, obj.height, obj.x, obj.y]
                    elif cls.__name__ == "Square":
                        attrs = [obj.id, obj.width, obj.x, obj.y]
                    else:
                        continue
                    writer.writerow(attrs)

    @classmethod
    def load_from_file_csv(cls):
        """
        This method reads a CSV file with the name of the class and creates
        a list of instances of that class from the data in the file.

        Returns:
            list: a list of instances of the class
        """

        filename = cls.__name__ + ".csv"

        with open(filename, "r") as f:
            if cls.__name__ == "Rectangle":
                reader = csv.DictReader(
                    f, fieldnames=['id', 'width', 'height', 'x', 'y'])
            elif cls.__name__ == "Square":
                reader = csv.DictReader(
                    f, fieldnames=['id', 'size', 'x', 'y'])

            instances = []
            for instance in reader:
                instance = {key: int(value) for key, value in instance.items()}
                temp = cls.create(**instance)
                instances.append(temp)

        return instances

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
            This method uses turtle graphics to draw
            the rectangles and squares in the lists.

        Parameters:
            list_rectangles (list): a list of Rectangle objects
            list_squares (list): a list of Square objects
        """

        t = turtle.Turtle()
        t.screen.bgcolor("#b7312c")
        t.pensize(5)
        t.shape("turtle")

        t.color("#ff0000")
        for rect in list_rectangles:
            t.showturtle()
            t.up()
            t.goto(rect.x, rect.y)
            t.down()
            for i in range(2):
                t.forward(rect.width)
                t.left(90)
                t.forward(rect.height)
                t.left(90)
            t.hideturtle()

        t.color("#00ff00")
        for sq in list_squares:
            t.showturtle()
            t.up()
            t.goto(sq.x, sq.y)
            t.down()
            for i in range(2):
                t.forward(sq.width)
                t.left(90)
                t.forward(sq.height)
                t.left(90)
            t.hideturtle()
