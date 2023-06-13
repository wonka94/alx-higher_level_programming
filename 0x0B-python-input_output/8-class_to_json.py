#!/usr/bin/python3
""" `class_to_json` module """


def class_to_json(obj):
    """Returns the dictionary description with simple
       data structure for JSON serialization of an object
    """
    desc = {}
    for key in obj.__dict__:
        value = getattr(obj, key)
        if type(value) in [list, dict, str, int, bool]:
            desc[key] = value

    return desc
