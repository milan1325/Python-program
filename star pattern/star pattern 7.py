n = int(input("enter a number : "))
for i in range(1,2*n):
    for j in range(1,2*n):
        if j==n+i-1 or j==n-i+1 or j==i-n+1 or j==3*n-i-1:
            print("1",end=" ")
        elif j==n or i==n:
            print("0",end=" ")
        else:
            print(" ",end=" ")
    print()


# import pandas as pd
# from matplotlib import pyplot as py
# x = pd.read_excel("marks.xlsx",usecols=["Name "])
# y = pd.read_excel("marks.xlsx",usecols=["TOTAL"])
# # py.bar(x,y)
# # py.show()
