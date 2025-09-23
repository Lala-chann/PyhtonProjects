import random
from dataclasses import replace
from itertools import combinations

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

def letter_logic(l,n,s):
    password = []
    for _ in range(l):
        choice_random = random.choice(letters)
        password.append(choice_random)


    for _ in range(n):
        choice_random = random.choice(numbers)
        password.append(choice_random)

    for _ in range(s):
        choice_random = random.choice(symbols)
        password.append(choice_random)

    return password

remover = letter_logic(nr_letters,nr_symbols,nr_numbers)
print(remover)
random.shuffle(remover)
print(remover)
print(f"Your password is : {"".join(remover)}")


