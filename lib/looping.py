#!/usr/bin/env python

def happy_new_year():
    for i in range(10, 0, -1):
        print(i)
    print("Happy New Year!")

def square_integers(lst):
    return [x ** 2 for x in lst]

def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

