"""
Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)
"""


def string_lists():
    print("Enter a word")
    chosen_string = input()
    reversed_string = chosen_string[::-1]

    if chosen_string == "":
        print("You did not enter a string of characters")
    elif chosen_string == reversed_string:
        print("These characters form a Palindrome")
    else:
        print("These characters do not form a Palindrome")


if __name__ == '__main__':
    string_lists()