#!/usr/bin/python3
def print_last_digit(number):
    digit = 0
    if number >= 0:
        print("{}".format(number % 10))
    else:
        print("{}".format(number % -10))
