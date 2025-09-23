
from art import*
from game_data import*
import random

def format_data(choice):
    name = choice['name']
    description = choice['description']
    country = choice['country']
    return f"{name}, {description}, {country}"


def intro(a_l, b_l):
    print(logo)
    print(f"Compare A: {format_data(a_l)}")
    print(vs)
    print(f"Against B: {format_data(b_l)}")

def game_logic(a, b):
    if a['follower_count'] > b['follower_count']:
        return "a"
    else:
        return "b"

a_list = random.choice(data)
b_list = random.choice(data)
score = 0

while True:
    intro(a_list,b_list)
    choice = input("Who has more follower? Type 'A' or 'B': ").lower()

    if game_logic(a_list,b_list) == choice:
        score += 1
        print(f"You are right!. Current score : {score}")

        if game_logic(a_list,b_list) == "a":
            new_a = random.choice(data)
            while new_a == a_list or new_a == b_list:
                new_a = random.choice(data)
            a_list = new_a
        else:
            new_b = random.choice(data)
            while new_b == b_list or new_b == a_list:
                new_b = random.choice(data)
            b_list = new_b
    else:
        print(f"Sorry! that was wrong. Final score: {score}")
        break





