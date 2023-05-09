#!/usr/bin/python3
def uppercase(str):
    result = ""
    for letter in str:
        if ord(letter) > 96 and ord(letter) < 123:
            result += chr(ord(letter) - 32)
        else:
            result += letter
    print("{}".format(result))
