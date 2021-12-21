#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    num = -number
else:
    num = number
n = num % 10
if n == 0:
    print("Last digit of {:d} is 0 and is 0".format(number, number % 10))
elif n < 6 or number < 0:
    print(
            "Last digit of {:d} is {:d} and is less than 6 and not 0".format
            (number, int((num % 10) * (number / num))))
else:
    print("Last digit of {:d} is {:d} and is greater than 5".format(number, n))
