#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or len(roman_string) == 0:
        return 0
    else:
        result = 0
        rn = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for c in roman_string.upper():
            if c in rom_values.keys():
                result += int(rn[c])
            else:
                return 0
        return int(result)
