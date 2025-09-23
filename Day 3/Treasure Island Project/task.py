print('''
                                                                    |
                                                                   ,( @' `
              _ _ -^- _ _                                                 |
            /             )/~^~" ',                                      @')
           (               )/`"`', `,                         |
           (               )  ,'"  ,`                      ( @' `
            )             (    `'"                               |
      _ - - (== === === ==) - - _             |\                @'),
     ( _  _ _ _ _ _ _ _ _ _ _ _ _ )       ,( @' `\
           /  ;    / ., ,. \   ;                 |
          / ;     ;  (o o)  ;   ;               @')       Mr RUSTY
          ;   ;   ;      _) ;   ;                         ~~~~~~~~
          ;       `,/;;;`:;;\  ;                      He looks after the
           ;, ,, , (.;;.,;,,;)'___ ___ ____ ___ _      Magic Roundabout
             "``'/`   " " '\                   / |     itself and plays
                /   _       |___ ____ ____  /  = |      the barrel organ.
               |  (   \O  O |             | c ~  |
               |   \   \    |  (@)        |   *  |
               |     \   \ _._  _       |  %   |
               |     | \ _ _*_|=)U@-      | (  + |
               |     | O  O |             |  //~'
               /     |      |             | ||    |
              (_ _ _ |_ _ _ _\            | || () |
                 |  `'|   |__ ___ ___ ____|/||    |
       -cfbd-    |    | __|/\                _./`
                 |____/\ ____)
                (_______)
''')
def direction_chose(ch):
    if ch == "right":
        print("Fall into a hole. Game Over.")
    else:
        swim_part = input("You've come to a lake. There is an island in the middle of the lake.\n "
                          'Type "wait" to wait for a boat. Type "swim" to swim across: ').lower()
        swim_or_wait(swim_part)

def swim_or_wait(swim_part):
    if swim_part == "swim":
        print("Attacked by trout. Game Over.")
    else:
        choice = input("You arrive at the island unharmed. There is a house with 3 doors.\n"
                            "One red, one yellow and one blue. Which colour do you choose?").lower()
        door_choice(choice)

def door_choice(choice):
    if choice == "red":
        print("Burned by fire. Game Over")
    elif choice == "blue":
        print("Eaten by beasts. Game Over.")
    elif choice == "yellow":
        print("You Won!")
    else:
        print("Game Over.")

print("""Welcome to Treasure Island.\n
Your mission is to find the treasure.\n
You're at a cross road. Where do you want to go?
""")
game= input('Type "left" or "right":\n')
direction_chose(game)
























