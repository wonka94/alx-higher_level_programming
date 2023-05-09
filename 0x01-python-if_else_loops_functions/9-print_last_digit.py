#!/usr/bin/python3
def print_last_digit(number):
    digit = 0
    if number >= 0:
        return number % 10
    else:
        return number % -10
