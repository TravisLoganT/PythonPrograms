"""
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the
first and last elements of the given list. For practice, write this code inside a function.
"""

import random


def make_list():
    random_list = random.sample(range(1, 100), 10)
    list_ends(random_list)


def list_ends(a):
    first_and_last = [a[0], a[-1]]

    print("Original List:", a)
    print("First and Last from that list:", first_and_last)


if __name__ == '__main__':
    make_list()
