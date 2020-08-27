import time


print("Welcome To The Table Printer")
print("You Just Need To Enter The Number, And We Will Print The Whole Table OF It")

def printer(unum):
    endnum = unum * 10 + 1
    i = 1
    mpl = [j for j in range(endnum) if j % unum == 0]
    for i in range(11):
        print(f"{unum}*{i} = {mpl[i]}")
        i = i + 1

    re = int(input("Do You Want To It Again?\nFor Again--1  For Exit--2\n:-"))
    if re == 1:
        unum = int(input("\nEnter The Number \n:-"))
        printer(unum)
    else:
        print("Thank You For Using Our Software!!\n\n")
        time.sleep(2)
        exit()

unum = int(input("Enter The Number \n:-"))
printer(unum)