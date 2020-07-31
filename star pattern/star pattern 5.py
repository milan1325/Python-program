

#    * * * * * *
#    *         *
#    *         *
#    *         *
#    *         *
#    * * * * * *

x = int(input("Enter a Number od Row : "))
y = int(input("Enter a Number od Column : "))           #i=x   and j=y
for i in range(1,x+1):
    for j in range(1,y+1):
        if i==1 or i==x:
            print("*", end=" ")
        elif (j==1 or j==y):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(" ")