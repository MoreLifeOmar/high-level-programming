# Test-driven development

# Learning Objectives

* What’s an interactive test
* Why tests are important
* How to write Docstrings to create tests
* How to write documentation for each module and function
* What are the basic option flags to create tests
* How to find edge cases

# Tasks

## Integers addition

Write a function that adds 2 integers.

* Prototype: `def add_integer(a, b=98):`
* `a` and `b` must be integers or floats, otherwise raise a `TypeError` exception with the message `a must be an integer` or `b must be an integer`
* `a` and `b` must be first casted to integers if they are float
* Returns an integer: the addition of `a` and `b`
* You are not allowed to import any module

**Solution:** [0-add_integer.py](https://github.com/omarcherni007/holbertonschool-higher_level_programming/blob/master/0x07-python-test_driven_development/0-add_integer.py), [tests/0-add_integer.txt](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x07-python-test_driven_development/tests/0-add_integer.txt)

```
$ omarcherni007@ubuntu:~/0x07$ cat 0-main.py
#!/usr/bin/python3
add_integer = __import__('0-add_integer').add_integer

print(add_integer(1, 2))
print(add_integer(100, -2))
print(add_integer(2))
print(add_integer(100.3, -2))
try:
    print(add_integer(4, "School"))
except Exception as e:
    print(e)
try:
    print(add_integer(None))
except Exception as e:
    print(e)

$ omarcherni007@ubuntu:~/0x07$ ./0-main.py
3
98
100
98
b must be an integer
a must be an integer
$ omarcherni007@ubuntu:~/0x07$ python3 -m doctest -v ./tests/0-add_integer.txt | tail -2
18 passed and 0 failed.
Test passed.
$ omarcherni007@ubuntu:~/0x07$ python3 -c 'print(__import__("0-add_integer").__doc__)' | wc -l
5
$ omarcherni007@ubuntu:~/0x07$ python3 -c 'print(__import__("0-add_integer").add_integer.__doc__)' | wc -l
3
```

## Divide a matrix

Write a function that divides all elements of a matrix.

* Prototype: `def matrix_divided(matrix, div):`
* `matrix` must be a list of lists of integers or floats, otherwise raise a `TypeError` exception with the message `matrix must be a matrix (list of lists) of integers/floats`
* Each row of the `matrix` must be of the same size, otherwise raise a `TypeError` exception with the message `Each row of the matrix must have the same size`
* `div` must be a number (integer or float), otherwise raise a `TypeError` exception with the message `div must be a number`
* `div` can’t be equal to `0`, otherwise raise a `ZeroDivisionError` exception with the message `division by zero`
* All elements of the matrix should be divided by `div`, rounded to 2 decimal places
* Returns a new matrix
* You are not allowed to import any module

**Solution:** [2-matrix_divided.py](https://github.com/omarcherni007/holbertonschool-higher_level_programming/blob/master/0x07-python-test_driven_development/2-matrix_divided.py), [tests/2-matrix_divided.txt](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x07-python-test_driven_development/tests/2-matrix_divided.txt)

```
$ omarcherni007@ubuntu:~/0x07$ cat 2-main.py
#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix_divided(matrix, 3))
print(matrix)

$ omarcherni007@ubuntu:~/0x07$ ./2-main.py
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
[[1, 2, 3], [4, 5, 6]]
$ omarcherni007@ubuntu:~/0x07$ python3 -m doctest -v ./tests/2-matrix_divided.txt | tail -2
36 passed and 0 failed.
Test passed.
$ omarcherni007@ubuntu:~/0x07$
```

## Say my name

Write a function that prints `My name is <first name> <last name>`

* Prototype: `def say_my_name(first_name, last_name=""):`
* `first_name` and `last_name` must be strings otherwise, raise a `TypeError` exception with the message `first_name must be a string` or `last_name must be a string`
* You are not allowed to import any module

**Solution:** [3-say_my_name.py](https://github.com/omarcherni007/holbertonschool-higher_level_programming/blob/master/0x07-python-test_driven_development/3-say_my_name.py), [tests/3-say_my_name.txt](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x07-python-test_driven_development/tests/3-say_my_name.txt)

```
$ omarcherni007@ubuntu:~/0x07$ cat 3-main.py
#!/usr/bin/python3
say_my_name = __import__('3-say_my_name').say_my_name

say_my_name("John", "Smith")
say_my_name("Walter", "White")
say_my_name("Bob")
try:
    say_my_name(12, "White")
except Exception as e:
    print(e)

$ omarcherni007@ubuntu:~/0x07$ ./3-main.py | cat -e
My name is John Smith$
My name is Walter White$
My name is Bob $
first_name must be a string$
$ omarcherni007@ubuntu:~/0x07$ python3 -m doctest -v ./tests/3-say_my_name.txt | tail -2
11 passed and 0 failed.
Test passed.
$ omarcherni007@ubuntu:~/0x07$
```

## Print square

Write a function that prints a square with the character #.

* Prototype: `def print_square(size):`
* `size` is the size length of the square
* `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
* if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
* if `size` is a float and is less than 0, raise a TypeError exception with the message `size must be an integer`
* You are not allowed to import any module

**Solution:** [4-print_square.py](https://github.com/omarcherni007/holbertonschool-higher_level_programming/blob/master/0x07-python-test_driven_development/4-print_square.py), [tests/4-print_square.txt](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x07-python-test_driven_development/tests/4-print_square.txt)

```
$ omarcherni007@ubuntu:~/0x07$ cat 4-main.py
#!/usr/bin/python3
print_square = __import__('4-print_square').print_square

print_square(4)
print("")
print_square(10)
print("")
print_square(0)
print("")
print_square(1)
print("")
try:
    print_square(-1)
except Exception as e:
    print(e)
print("")

$ omarcherni007@ubuntu:~/0x07$ ./4-main.py
####
####
####
####

##########
##########
##########
##########
##########
##########
##########
##########
##########
##########


#

size must be >= 0

$ omarcherni007@ubuntu:~/0x07$ python3 -m doctest -v ./tests/4-print_square.txt
$ omarcherni007@ubuntu:~/0x07$
```

## Text indentation

Write a function that prints a text with 2 new lines after each of these characters: `.`, `?` and `:`

* Prototype: `def text_indentation(text):`
* `text` must be a string, otherwise raise a `TypeError` exception with the message `text must be a string`
* There should be no space at the beginning or at the end of each printed line
* You are not allowed to import any module

**Solution:** [5-text_indentation.py](https://github.com/omarcherni007/holbertonschool-higher_level_programming/blob/master/0x07-python-test_driven_development/5-text_indentation.py), [tests/5-text_indentation.txt](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x07-python-test_driven_development/tests/5-text_indentation.txt)

## Max integer - Unittest

Since the beginning you have been creating “Interactive tests”. For this exercise, you will add Unittests.

In this task, you will write unittests for the function `def max_integer(list=[]):`.

* Your test file should be inside a folder `tests`
* You have to use the [unittest module](https://docs.python.org/3/library/unittest.html#module-unittest)
* Your test file should be python files (extension: `.py`)
* Your test file should be executed by using this command: `python3 -m unittest tests.6-max_integer_test`
* All tests you make must be passable by the function below
* We strongly encourage you to work together on test cases, so that you don’t miss any edge case

**Solution:** [tests/6-max_integer_test.py](https://github.com/omarcherni007/holbertonschool-higher_level_programming/blob/master/0x07-python-test_driven_development/tests/6-max_integer_test.py)

```
$ omarcherni007@ubuntu:~/0x07$ cat 6-max_integer.py
#!/usr/bin/python3
"""Module to find the max integer in a list
"""


def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result

$ omarcherni007@ubuntu:~/0x07$ 
$ omarcherni007@ubuntu:~/0x07$ cat 6-main.py
#!/usr/bin/python3
max_integer = __import__('6-max_integer').max_integer

print(max_integer([1, 2, 3, 4]))
print(max_integer([1, 3, 4, 2]))
$ omarcherni007@ubuntu:~/0x07$
$ omarcherni007@ubuntu:~/0x07$ ./6-main.py
4
4
$ omarcherni007@ubuntu:~/0x07$
$ omarcherni007@ubuntu:~/0x07$ python3 -m unittest tests.6-max_integer_test 2>&1 | tail -1
OK
$ omarcherni007@ubuntu:~/0x07$
$ omarcherni007@ubuntu:~/0x07$ head -7 tests/6-max_integer_test.py 
#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
$ omarcherni007@ubuntu:~/0x07$
```
