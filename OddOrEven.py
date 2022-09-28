"""Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message
to the user.

Extras:

If the number is a multiple of 4, print out a different message.

Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
"""


def odd_or_even():
    print("What number would you like to use?")
    number = int(input())

    if number % 2 == 0:
        print("This number is even")
    elif number % 2 != 0:
        print("This number is odd")

    multiple_of_4(number)


def multiple_of_4(number):
    if number % 4 == 0:
        print("This number is a multiple of 4")
    else:
        print("This number is not a multiple of 4")


def divides_evenly():
    print("Enter a number")
    num = int(input())
    print("Enter another number")
    check = int(input())

    if num % check == 0:
        print(str(num) + " divides evenly into " + str(check))
    else:
        print(str(num) + " does not divide evenly into " + str(check))


if __name__ == '__main__':
    odd_or_even()
    divides_evenly()