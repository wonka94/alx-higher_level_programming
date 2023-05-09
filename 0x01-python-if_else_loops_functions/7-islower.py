#!/usr/bin/python3
def islower(c):
    for letter in range(ord('a'), ord('z')+1):
        if chr(c) == chr(letter):
            return True
        else:
            return False
