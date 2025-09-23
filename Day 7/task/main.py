import random
from hangman_art import*
from hangman_words import*

print(logo)
create_word_list = random.choice(word_list)
letter = []
lives = 6

def word_to_guess(w):
    display = "_" * len(w)
    print(f"Word to guess: {display}")

game_start = True
while game_start:
    word_to_guess(create_word_list)
    guess = input("Guess a letter: ")

    if guess not in letter:
        letter.append(guess)

        if guess not in create_word_list:
            lives -= 1
            print(f"You guessed {guess}, that is not in the word. You lose a life.")

            print(stages[lives])  # or print(stages[lives-1]) depending on your stages array
            print("*" * 20 + f"{lives}/6 LIVES LEFT" + "*" * 20)


    position = ""
    for items in create_word_list:
        if items in letter:
            position += items
        else:
            position += "_"
    print(position)



    if "_" not in position:
        game_start= False
        print("*" * 19 + "YOU WON. CONGRATULATION!"+ "*" * 19)
    elif lives == 0:
        game_start = False
        print("*" * 19 + "IT WAS galaxy! YOU LOSE" + "*" * 19)







