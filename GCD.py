def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

a = int(input("Enter a first Number : "))
b = int(input("Enter a second number : "))
print("gcd of {} and {} is :".format(a,b),gcd(a,b))

print("lcm of {} and {} is :".format(a,b),(a*b/gcd(a,b)))

