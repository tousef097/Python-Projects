import random
def guess_number():
    print("Welcome To The Number Guessing Game")
    print("You Have 10 Chance To Guess The Number.. (The Number is between 1-50)")
    print("Enter Your First Guess For The Number")
    gnum = random.randint(1, 50)
    finpu = int(input(":-"))

    if(finpu>gnum):
        print("Wrong!!! You Select A Greater Number")
        print("9 Chances Left")
        print("\nEnter A New Number")
        finpu = int(input(":-"))

    elif(finpu<gnum):
        print("Wrong!!! You Select A Lesser Number")
        print("9 Chances Left")
        print("\nEnter A New Number")
        finpu = int(input(":-"))


    if (finpu > gnum):
        print("Wrong!!! You Select A Greater Number")
        print("8 Chances Left")
        print("\nEnter A New Number")
        finpu = int(input(":-"))

    elif (finpu < gnum):
        print("Wrong!!! You Select A Lesser Number")
        print("8 Chances Left")
        print("\nEnter A New Number")
        finpu = int(input(":-"))


    if (finpu > gnum):
        print("Wrong!!! You Select A Greater Number")
        print("7 Chances Left")
        print("\nEnter A New Number")
        finpu = int(input(":-"))

    elif (finpu < gnum):
        print("Wrong!!! You Select A Lesser Number")
        print("7 Chances Left")
        print("\nEnter A New Number")
        finpu = int(input(":-"))

    if (finpu > gnum):
        print("Wrong!!! You Select A Greater Number")
        print("6 Chances Left")
        print("\nEnter A New Number")
        finpu = int(input(":-"))

    elif (finpu < gnum):
        print("Wrong!!! You Select A Lesser Number")
        print("6 Chances Left")
        print("\nEnter A New Number")
        finpu = int(input(":-"))

    if (finpu > gnum):
        print("Wrong!!! You Select A Greater Number")
        print("5 Chances Left")
        print("\nEnter A New Number")
        finpu = int(input(":-"))

    elif (finpu < gnum):
        print("Wrong!!! You Select A Lesser Number")
        print("5 Chances Left")
        print("\nEnter A New Number")
        finpu = int(input(":-"))

    if (finpu > gnum):
        print("Wrong!!! You Select A Greater Number")
        print("4 Chances Left")
        print("\nEnter A New Number")
        finpu = int(input(":-"))

    elif (finpu < gnum):
        print("Wrong!!! You Select A Lesser Number")
        print("4 Chances Left")
        print("\nEnter A New Number")
        finpu = int(input(":-"))

    if (finpu > gnum):
        print("Wrong!!! You Select A Greater Number")
        print("3 Chances Left")
        print("\nEnter A New Number")
        finpu = int(input(":-"))

    elif (finpu < gnum):
        print("Wrong!!! You Select A Lesser Number")
        print("3 Chances Left")
        print("\nEnter A New Number")
        finpu = int(input(":-"))


    if (finpu > gnum):
        print("Wrong!!! You Select A Greater Number")
        print("2 Chances Left")
        print("\nEnter A New Number")
        finpu = int(input(":-"))

    elif (finpu < gnum):
        print("Wrong!!! You Select A Lesser Number")
        print("2 Chances Left")
        print("\nEnter A New Number")
        finpu = int(input(":-"))

    if (finpu > gnum):
        print("Wrong!!! You Select A Greater Number")
        print("It's Your Last Chance")
        print("\nEnter A Last Number")
        finpu = int(input(":-"))

    elif (finpu < gnum):
        print("Wrong!!! You Select A Lesser Number")
        print("It's Your Last Chance")
        print("\nEnter A Last Number")
        finpu = int(input(":-"))

    if (finpu!=gnum):
        print("\nGame Over")
        print("You Can't Guess The Number")

    else:
        print("\nCongratulation!! You Win The Game")

    print("Thanks For Playing This Game")
    print("\nDo you Want to play it again??\n     Play--1 , Exit--2")
    more = int(input(":-"))
    if more==1:
        print(guess_number())
    else:
        print("Exiting....")
        exit()

print(guess_number())
