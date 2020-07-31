i=0
for i in range(1,10):
    user=int(input("enter a guess number : "))
    if user>20:
        print("enter a smaller number")
    elif user<20:
        print("enter a bigger number")
    elif user==20:
        print(" ")
        print("wow! congratulation your guess number is right")
        break
    i=i+1
if user>20 or user<20:
    print(" ")
    print("your try is over better luck for next time")
