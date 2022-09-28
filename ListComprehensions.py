"""
Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.
"""

given_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

if __name__ == '__main__':
    new_list = [num for num in given_list if num % 2 == 0]
    print(new_list)
