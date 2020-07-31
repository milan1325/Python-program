i = int(input("Enter the Number of row : "))
j = int(input("Enter the Number of column : "))
# print(n)
for i in range (1,i+1):
    for j in range (1,j+1):
        if i<=j:
            print("*",end=' ')
    print(" ")