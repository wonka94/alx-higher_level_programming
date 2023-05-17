#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_list = dict(sorted(a_dictionary.items()))
    for key, value in new_list.items():
        print("{}: {}".format(key, value))
