#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = number % 10
if digit > 5:
    print(f"Last digit of {number} is {digit} and is greater than 5")
elif digit % 10 < 6 and digit != 0:
    print(f"Last digit of {number} is {digit} and "
          f"is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {digit} and is 0")
