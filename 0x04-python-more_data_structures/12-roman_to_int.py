#!/usr/bin/python3
def roman_to_int(roman_string):
    if len(roman_string) <= 0:
        return 0
    else:
        result = 0
        rn = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for c in roman_string:
            result += rn[c]
        return int(result)
