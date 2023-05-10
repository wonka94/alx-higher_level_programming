#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = ""
    for letter in str:
        if str[n]:
            continue
        new_str += letter
    return new_str
