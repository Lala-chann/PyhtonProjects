import random

from art import*
print(logo)
print("Welcome to the number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

def easy_game():
    print("You have 10 attempts remaining to guess the number.")
    random_number = random.randint(1,100)
    attempt = 10

    while attempt > 0:
        guess = int(input("Make a guess: "))


        if random_number == guess:
            print("You won!")
            break
        else:
            attempt -= 1
            print(f"You have {attempt} attempts remaining to guess the number.")

            if random_number > guess:
                print("too low")
                print("Guess again")
            else:
                print("Too high")
                print("Guess again")

    if attempt == 0:
        print("You are out of the attempt. Try again")




def hard_game():
    print("You have 5 attempts remaining to guess the number.")
    random_number = random.randint(1,100)
    attempt = 5

    while attempt > 0:
        guess = int(input("Make a guess: "))

        if random_number == guess:
            print("You won!")
            break
        else:
            attempt -= 1
            print(f"You have {attempt} attempts remaining to guess the number.")

            if random_number > guess:
                print("too low")
                print("Guess again")
            else:
                print("Too high")
                print("Guess again")

    if attempt == 0:
        print("You are out of attempt. Try again")


choice_logic = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if choice_logic == "easy":
    easy_game()
else:
    hard_game()





