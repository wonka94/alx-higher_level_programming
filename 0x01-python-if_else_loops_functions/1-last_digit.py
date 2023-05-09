#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number % 10 > 5:
    print(f"Last digit of {number:d} is {number[-1]:d} and is greater than 5")
elif number % 10 < 6 and number[-1] != 0:
    print(f"Last digit of {number:d} is {number[-1]:d} and "
          f"is less than 6 and not 0")
else:
    print(f"Last digit of {number:d} is {number[-1]:d} and is 0")
