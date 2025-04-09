from game1 import Game_1
from game2 import Game_2
print("Welcome to the Brain Games!")
print("May I have your name")
Name = input()
print("Hallo,", Name)
Game = [Game_1, Game_2]

gam = 1
while ( gam != 0 ):
    print("Stop game - 0, NOK - 1, Geometric progression - 2")
    gam = int(input("Choose a game:"))
    if ( gam > 0 and gam <= len(Game)):
        
        answer_true = Game[gam - 1]()
        for i in range(3, 0, -1):
            answer = input("Your answer: ")
            if (answer == answer_true):
                print("Correct!")
                break
            else:
                print("Not correct!   :(")
                print("You have popitoc:", i - 1   ,":(")

    elif (gam == 0):
        break
    else:
        print("Please choose from the list")


    

    
