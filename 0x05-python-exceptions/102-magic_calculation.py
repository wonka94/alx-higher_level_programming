#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    for i in range(3):
        try:
            if i > a:
                raise Exception("Too far")
            else:
                result = result + (a**b) / i
        except Exception:
            result = a + b
            break
    return result
