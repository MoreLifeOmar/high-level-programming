#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print(number,"is positive\n")
if number == 0:
    print(number,"is zero\n")
if number < 0:
    print(number,"is negative\n")
