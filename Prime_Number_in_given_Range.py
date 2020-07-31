n1 = int(input("enter a first number : "))
n2 = int(input("enter a second number : "))
count = 0
prime_number = []
for j in range(n1,n2+1):
    if j>1:
        count=0
        for n in range(2,j):
            if j%n==0:
                count+=1
                break
        if count==0:
            prime_number.append(j)
            # print(j)

print(prime_number)
lenth = len(prime_number)
print("Number of element in prime number : ",lenth)

