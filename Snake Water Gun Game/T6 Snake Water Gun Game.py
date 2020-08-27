# Snake Water Gun
# 10 times
# Point Count

import random

S = "Snake"
G = "Gun"
W = "Water"

count = 1

print("This is a game called Snake, Water, Gun..")
userpoint = 0
compoint = 0

while count<11:

    print("Please, Select Anything From\nS---Snake, G---Gun, W---Water..(Enter S or W or G)")
    userin = input()
    capuserin = userin.capitalize()
    # com = random.choice("S" "W")
    com = "W"
    if capuserin=="S" and com=="S":
        print("You Select Snake And Computer Select Also Snake")
        print("You Select As Same As Computer, So no one get any points")
        print("Computer Point = " , compoint)
        print("Your Point = ", userpoint)
        print("Chance Left = ", 10-count, "\n")

    elif capuserin=="W" and com=="W":
        print("You Select Water And Computer Select Also Water")
        print("You Select As Same As Computer, So no one get any points")
        print("Computer Point = ", compoint)
        print("Your Point = ", userpoint)
        print("Chance Left = ", 10 - count, "\n")

    elif capuserin=="G" and com=="G":
        print("You Select Gun And Computer Select Also Gun")
        print("You Select As Same As Computer, So no one get any points")
        print("Computer Point = ", compoint)
        print("Your Point = ", userpoint)
        print("Chance Left = ", 10 - count, "\n")

    elif capuserin=="S" and com=="W":
        print("You Select Snake And Computer Select Water")
        print("Snake Can Eat The Water, That Means You Win")
        print("Computer Point = ", compoint)
        userpoint =  userpoint+1
        print("Your Point = ", userpoint)
        print("Chance Left = ", 10 - count, "\n")

    elif capuserin=="S" and com=="G":
        print("You Select Snake And Computer Select Gun")
        print("Snake Can killen The Water, That Means You lose")
        compoint =  compoint+1
        print("Computer Point = ", compoint)
        print("Your Point = ", userpoint)
        print("Chance Left = ", 10 - count, "\n")

    elif capuserin=="W" and com=="S":
        print("You Select Water And Computer Select Snake")
        print("Snake Can Eat The Water, That Means You Lose")
        compoint =  compoint+1
        print("Computer Point = ", compoint)
        print("Your Point = ", userpoint)
        print("Chance Left = ", 10 - count, "\n")

    elif capuserin=="W" and com=="G":
        print("You Select Water And Computer Select Gun")
        print("Gun Can Do Nothing With The Water, That Means You Win")
        userpoint =  userpoint+1
        print("Computer Point = ", compoint)
        print("Your Point = ", userpoint)
        print("Chance Left = ", 10 - count, "\n")

    elif capuserin=="G" and com=="S":
        print("You Select Gun And Computer Select Snake")
        print("Snake Can be killen by The Gun, That Means You Win")
        userpoint =  userpoint+1
        print("Computer Point = ", compoint)
        print("Your Point = ", userpoint)
        print("Chance Left = ", 10 - count, "\n")

    elif capuserin=="G" and com=="W":
        print("You Select Gun And Computer Select Water")
        print("Gun Can Do Nothing With The Water, That Means You lose")
        compoint =  compoint+1
        print("Computer Point = ", compoint)
        print("Your Point = ", userpoint)
        print("Chance Left = ", 10 - count, "\n")
    count = count+1



if userpoint>compoint:
    print("Congatulations!! You Won This Game")

elif userpoint==compoint:
    print("The Match Is Draw, Play Again..")

else:
   print("You Lose The Game", "Because You Score = ", userpoint, "And Computer Score = ", compoint)