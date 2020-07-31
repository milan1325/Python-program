# import datetime
# c = datetime.datetime.now()
# with open("milan.txt","r+") as f:
#     f.write(str([str(c)]) + ":" + " Milan is a good Boy. \n")
#     for i in f:
#         print(i, end="")

import datetime
d = datetime.datetime.now()

def again():
    print("\n")
    again = input("DO YOU WANT TO USE AGAIN THIS SYSTERM \n"
                  "PLEASE TYPE \'Y\' FOR YES OR \'N\' FOR NO : ")
    if again == 'Y' or again == 'y':
        health()
    elif again == 'N' or again == 'n':
        print("THANK YOU")
        print("SEE YOU LATER")
    else:
        print("type a invaliad key")

def health():
    def log(k):
        if k== 1:
            c = int(input("For \'FOOD\' press 1 or For \'EXCERSIES\' press 2 : "))
            if c == 1:
                with open("milan_food.txt","a") as f:
                    value = input("TYPE HERE\n")
                    f.write(str([str(d)]) + " : " + value + "\n")
                    print("TYPE SUCESSFULLY")
            elif c == 2:
                with open("milan_excersies.txt","a") as f:
                    value = input("TYPE HERE\n")
                    f.write(str([str(d)]) + " : " + value + "\n")
                    print("TYPE SUCESSFULLY")
            else:
                print("YOUR INPUT IS WORNG \'press 1 or 2 only\'")
        elif k == 2:
            c = int(input("For \'FOOD\' press 1 or For \'EXCERSIES\' press 2 : "))
            if c == 1:
                with open("nirav_food.txt", "a") as f:
                    value = input("TYPE HERE\n")
                    f.write(str([str(d)]) + " : " + value + "\n")
                    print("TYPE SUCESSFULLY")
            elif c == 2:
                with open("nirav_excersies.txt", "a") as f:
                    value = input("TYPE HERE\n")
                    f.write(str([str(d)]) + " : " + value + "\n")
                    print("TYPE SUCESSFULLY")
            else:
                print("YOUR INPUT IS WORNG \'press 1 or 2 only\'")
        elif k == 3:
            c = int(input("For \'FOOD\' press 1 or For \'EXCERSIES\' press 2 : "))
            if c == 1:
                with open("keyur_food.txt", "a") as f:
                    value = input("TYPE HERE\n")
                    f.write(str([str(d)]) + " : " + value + "\n")
                    print("TYPE SUCESSFULLY")
            elif c == 2:
                with open("keyur_excersies.txt", "a") as f:
                    value = input("TYPE HERE\n")
                    f.write(str([str(d)]) + " : " + value + "\n")
                    print("TYPE SUCESSFULLY")
            else:
                print("YOUR INPUT IS WORNG \'press 1 or 2 only\'")
        else:
            print("only you can enter 1,2 or 3 ")

    def retreve(k):
        if k== 1:
            c = int(input("For \'FOOD\' press 1 or For \'EXCERSIES\' press 2 : "))
            if c == 1:
                with open("milan_food.txt") as f:
                    for i in f:
                        print(i,end="")
            elif c == 2:
                with open("milan_excersies.txt") as f:
                    for i in f:
                        print(i, end="")
            else:
                print("YOUR INPUT IS WORNG \'press 1 or 2 only\'")
        elif k == 2:
            c = int(input("For \'FOOD\' press 1 or For \'EXCERSIES\' press 2 : "))
            if c == 1:
                with open("nirav_food.txt") as f:
                    for i in f:
                        print(i, end="")
            elif c == 2:
                with open("nirav_excersies.txt") as f:
                    for i in f:
                        print(i, end="")
            else:
                print("YOUR INPUT IS WORNG \'press 1 or 2 only\'")
        elif k == 3:
            c = int(input("For \'FOOD\' press 1 or For \'EXCERSIES\' press 2 : "))
            if c == 1:
                with open("keyur_food.txt") as f:
                    for i in f:
                        print(i, end="")
            elif c == 2:
                with open("keyur_excersies.txt") as f:
                    for i in f:
                        print(i, end="")
            else:
                print("YOUR INPUT IS WORNG \'press 1 or 2 only\'")
        else:
            print("only you can enter 1,2 or 3 ")


    print("...WEL-COME TO  HEALTH MANAGMENT SYSTERM...")
    print("-----------------------------------------------------------------------------------------")
    first = int(input("For \'LOG\' press 1 or \'RETREVE\' press 2 : "))
    if first == 1:
        b = int(input("For \'MILAN\' press 1 or For \'NIRAV\' press 2 or For \'KEYUR\' press 3 :"))
        log(b)
    elif first == 2:
        b = int(input("For \'MILAN\' press 1 or For \'NIRAV\' press 2 or For \'KEYUR\' press 3 :"))
        retreve(b)
    else:
        print("SORRY!!!.....Your input is wrong ")

    again()


health()
input("press \'ENTER\' to quite :")

