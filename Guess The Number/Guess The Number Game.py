import random

num = random.randint(1, 50)
remaining_moves = 10
print(f"Welcome to the Guessing Game , You have {remaining_moves} moves remaining!!")
while True:
    remaining_moves -= 1
    print("Please Guess a number : ", end="")
    n = int(input())
    if n == num :
        print("Congratulations , You have won the Game")
        break
    elif n > num :
        print("Oh!! .You were close the answer,Let me give you a hint! , the answer is less than your number")
        if remaining_moves == 0 :
            print(f"Sorry , You don't have any moves left, Answer was{num}")
            break
        print(f"Don't Worry you have {remaining_moves} moves left")
    else :
        print("Oh!! .You were close the answer,Let me give you a hint! , the answer is greater than your number")
        if remaining_moves == 0 :
            print(f"Sorry , You don't have any moves left, Answer was {num} ")
            break
        print(f"Don't Worry you have {remaining_moves} moves left")
