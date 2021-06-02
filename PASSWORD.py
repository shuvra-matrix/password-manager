from random import *

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def passwords():
    random_later = randint(6, 10)
    random_number = randint(2, 6)
    random_symbol = randint(3, 6)

    password_list = []

    for letter in range(random_later):
        password_list.append(choice(letters))

    for number in range(random_number):
        password_list.append(choice(numbers))

    for symbol in range(random_symbol):
        password_list.append(choice(symbols))

    shuffle(password_list)

    password = ""

    for passwords in password_list:
        password += passwords
    return password
