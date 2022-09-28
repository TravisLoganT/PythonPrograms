"""
Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
"""


def divisor():
    print("Input a number")
    number = int(input())
    possible_divisors = list(range(2, number))
    actual_divisors = []

    for divisors in possible_divisors:
        if number % divisors == 0:
            actual_divisors.append(divisors)

    if number == 0:
        print("0 will have no divisors as that would be undefinable")
    elif number < 0:
        print("Please enter a positive number")
    elif actual_divisors != []:
        print(number, "Has the divisors of", actual_divisors)
    else:
        print("This number is a prime number, so it has no divisors")


if __name__ == '__main__':
    divisor()
