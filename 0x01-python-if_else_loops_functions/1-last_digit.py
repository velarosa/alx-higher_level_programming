#!/usr/bin/python3
import random
number = random.randint(-100, 100)
lastdigit = int(repr(number)[-1])
if lastdigit > 5:
    print(f"Last digit of {number:} is {lastdigit} and is greater than 5")
elif lastdigit == 0:
    print(f"Last digit of {number:} is {lastdigit} and is 0")
else:
    print(f"Last digit of {number:} is {lastdigit} and is less than 6 and not 0")
