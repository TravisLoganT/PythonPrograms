
def get_number():
    print("Please enter a number")
    number = int(input())
    is_prime(number)


def is_prime(num):
    potential_divisors = list(range(2, num))
    actual_divisors = []

    for number in potential_divisors:
        if num % number == 0:
            actual_divisors.append(number)

    if actual_divisors:
        print("This is not a prime number")
    else:
        print("This is a prime number")


if __name__ == '__main__':
    get_number()
