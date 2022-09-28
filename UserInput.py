def name_input():
    print("Hello there, What is your name?")
    name = input()
    name_message = "Nice to meet you, " + name
    print(name_message)
    age_input(name)


def age_input(name):
    print("How are old are you " + name)
    age = input()
    years_to_100 = 100 - int(age)
    print("Oh Wow! Did you know that you will be 100 in " + str(years_to_100) + " years")
    print("That would be the year of " + str(2022 + years_to_100))
    email_input(name)


def email_input(name):
    print("What is your email address " + name + "?")
    email_address = input()
    print("Is " + email_address + " correct? Y/N")

    while True:
        is_correct = input()
        if is_correct == 'Y':
            print("Thank you")
            break
        elif is_correct == 'N':
            email_input(name)
        else:
            print("That is not a valid input, Please try again")

    print("Expected Stop")


if __name__ == '__main__':
    name_input()
