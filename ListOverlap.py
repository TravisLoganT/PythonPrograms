"""
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists
(without duplicates). Make sure your program works on two lists of different sizes.

Extras:

Randomly generate two lists to test this

Write this in one line of Python

"""

import random


def list_overlap():
    list_one = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    list_two = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    conjoined_list = []

    for number_of_one in list_one:
        for number_of_two in list_two:
            # This will remove duplicates as it checks if the number is already in the list
            if number_of_two == number_of_one and number_of_two not in conjoined_list:
                conjoined_list.append(number_of_two)

    print(conjoined_list)


def random_list_overlap():
    # Takes a sample within the given range and take a random number from a given set
    random_list_one = random.sample(range(1, 50), random.randint(1, 20))
    random_list_two = random.sample(range(1, 50), random.randint(1, 20))
    random_conjoined_list = []

    print("List one:", random_list_one)
    print("List two:", random_list_two)

    for random_number_in_one in random_list_one:
        for random_number_in_two in random_list_two:
            if random_number_in_two == random_number_in_one and random_number_in_two not in random_conjoined_list:
                random_conjoined_list.append(random_number_in_two)

    if random_conjoined_list:
        print("Overlaps:", random_conjoined_list)
    else:
        print("There are no commons numbers present within these two lists.")


if __name__ == '__main__':
    list_overlap()
    random_list_overlap()
