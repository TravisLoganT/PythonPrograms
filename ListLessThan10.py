"""
Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.

Extras:

Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in
it and print out this new list.

Write this in one line of Python.

Ask the user for a number and return a list that
contains only elements from the original list a that are smaller than that number given by the user. """


example_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


# This will print the number individually as they are compared to being less than 5
def less_than_10():
    for number in example_list:
        if number < 5:
            print(number)


# This will add the numbers that are less than 5 to a list, and print the list as a whole
def new_list_less_than_10():
    new_list = []
    for number in example_list:
        if number < 5:
            new_list.append(number)
    print(new_list)


# Does the function new_list_less_than_10() but all on one line
def new_list_one_line():
    print([number for number in example_list if number < 5])


# Function to return a list of numbers from the original list that are less than a number that the user inputs
def user_input_function():
    numbers_less_than_choice = []
    print("Enter a number")
    number_choice = int(input())

    for number in example_list:
        if number < number_choice:
            numbers_less_than_choice.append(number)
    print("The numbers that are less than your chosen number are:", numbers_less_than_choice)


if __name__ == "__main__":
    less_than_10()
    new_list_less_than_10()
    new_list_one_line()
    user_input_function()
