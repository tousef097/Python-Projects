# Health Managment System
# 3 clients - Kaushal, Bappon, Shubam
# total 6 files
# # ** def getdate():
#         import datetime
#         return datetime.datetime.now()
# Write a function that when executed takes as input client name..

def getdate():
         import datetime
         return datetime.datetime.now()

def health():
    print("What you want? Input in log? or View your Log?")
    print("For Input In Log--Enter 1 \nFor View Log--Enter 2")
    wantinpu = int(input(":-"))
    if wantinpu==1 :
        print("Enter you name code")
        print("Kaushal-1, Bappon-2, Shubam-3")
        namein = int(input(":-"))
        if namein==1:
            print(" Hii Kaushal.. Where You Want to Add??")
            print(" Enter--1 for Eating Log \n Enter--2 For Exercise Log")
            wherelog = int(input(":-"))
            if wherelog==1 :
                print("Enter What You Eat")
                eatkaushal = input(":-")
                lek = open("T5 Log Eat Kaushal.txt", "a")
                lek.write(str(getdate()))
                lek.write(eatkaushal + "\n")
                lek.close()

            elif wherelog==2 :
                print("Enter What Exercise You Did?")
                exerkaushal = input(":-")
                lpk = open("T5 Log Exercise Kaushal.txt", "a")
                lpki = lpk.writelines(str(getdate()) + " " + exerkaushal + "\n")
                lpk.close()

        elif namein==2:
                print(" Hii Bappon.. Where You Want to Add??")
                print(" Enter--1 for Eating Log \n Enter--2 For Exercise Log")
                wherelog = int(input(":-"))
                if wherelog == 1:
                    print("Enter What You Eat")
                    eatbappon = input(":-")
                    leb = open("T5 Log Eat Bappon.txt", "a")
                    lebi = leb.write(str(getdate())+ " " + eatbappon + "\n")
                    leb.close()

                elif wherelog == 2:
                    print("Enter What Exercise You Did?")
                    exerbappon = input(":-")
                    lpb = open("T5 Log Exercise Bappon.txt", "a")
                    lpbi = lpb.write(str(getdate()) + " " +  exerbappon + "\n")
                    lpb.close()


        elif namein==3:
                print(" Hii Shubam.. Where You Want to Add??")
                print(" Enter--1 for Eating Log \n Enter--2 For Exercise Log")
                wherelog = int(input())
                if wherelog == 1:
                    print("Enter What You Eat")
                    eatshubam = input(":-")
                    les = open("T5 Log Eat Shubam.txt", "a")
                    lesi = les.write(str(getdate()) + " " + eatshubam + "\n")
                    les.close()

                elif wherelog == 2:
                    print("Enter What Exercise You Did?")
                    exershubam = input(":-")
                    lps = open("T5 Log Exercise Shubam.txt", "a")
                    lpsi = lps.write(str(getdate()) + " " + exershubam + "\n")
                    lps.close()

    elif wantinpu==2:
        print("Who's Log You Want To See??")
        print("Enter The Name Code \nKaushal-1, Bappon-2, Shubam-3")
        namein = int(input(":-"))
        if namein == 1:
            print(" It's Kaushal's Log.. What You Want to See?")
            print(" Enter--1 for Eating Log \n Enter--2 For Exercise Log")
            wherelog = int(input(":-"))
            if wherelog == 1:
                lek = open("T5 Log Eat Kaushal.txt", "r")
                leki = print(lek.readline())
                lek.close()
            elif wherelog == 2:
                lpk = open("T5 Log Exercise Kaushal.txt", "r")
                lpki = print(lpk.readline())
                lpk.close()

        elif namein == 2:
            print(" It's Bappon's Log.. What You Want to See?")
            print(" Enter--1 for Eating Log \n Enter--2 For Exercise Log")
            wherelog = int(input(":-"))
            if wherelog == 1:
                leb = open("T5 Log Eat Bappon.txt", "r")
                lebi = print(leb.readline())
                leb.close()
            elif wherelog == 2:
                lpb = open("T5 Log Exercise Bappon.txt", "r")
                lpbi = print(lpb.readline())
                lpb.close()

        elif namein == 3:
            print(" It's Shubam's Log.. What You Want to See?")
            print(" Enter--1 for Eating Log \n Enter--2 For Exercise Log")
            wherelog = int(input(":-"))
            if wherelog == 1:
                les = open("T5 Log Eat Shubam.txt", "r")
                lesi = print(les.readline())
                les.close()
            elif wherelog == 2:
                lps = open("T5 Log Exercise Shubam.txt", "r")
                lpsi = print(lps.readline())
                lps.close()

    res = int(input("What You Want To Do??\n1--Restart, 2--Exit\n:-"))
    if res==1:
        print(health())
    elif res==2:
        exit()

print(health())