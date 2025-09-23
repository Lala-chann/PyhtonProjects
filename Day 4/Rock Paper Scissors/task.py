import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
def human_gamer(g):
    if g == 0:
        print(rock)
        return 0
    elif g == 1:
        print(paper)
        return 1
    else:
        print(scissors)
        return 2

def computer_gamer():
    print("computer choice")
    choice = random.randint(0,2)
    if choice == 0:
        print(rock)
    elif choice == 1:
        print(paper)
    else:
        print(scissors)
    return choice

def game_logic(human, computer):
    if human == computer:
        print("It is draw!")
    elif (human == 0 and computer == 2) or (human == 1 and computer == 0) or (human == 2 and computer == 1):
        print("You won!")
    else:
        print("You lost!")



start = int(input("What do you choose? Type 0 for rock, 1 for paper,2 for scissors? "))
human_gamer(start)
computer_choice = computer_gamer()
game_logic(start,computer_choice)







