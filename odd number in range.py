n1 = int(input("Enter a first number : "))
n2 = int(input("Enter a second number : "))
odd_number = []
for i in range(n1,n2+1):
    if i%2!=0:
        odd_number.append(i)

print(odd_number)

