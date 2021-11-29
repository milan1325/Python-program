from math import exp
import matplotlib.pyplot as plt
import numpy as np

def fact(x):
    if x==0:
        return 1
    else:
        return (fact(x-1)*x)

def poisson(x,lembda):
    prob = exp(-lembda)*lembda**x/fact(x)
    return prob
    
if __name__ == "__main__" :
    obs = int(input("Enter a number of observation (< 172): "))
    probs = []
    x = []

    for i in range(0,obs):
        x.append(i)

    sum = 0
    for a in x:
        sum = sum + a

    n = len(x)

    lembda = sum/n

    for i in range(0,obs):
        probability = poisson(i,lembda)
        probs.append(probability)

plt.plot(x,probs,color="red")
plt.xlabel("Data points")
plt.ylabel("Probability Mass Function")
plt.title("Poisson Distribution")
plt.show()

print(probs)
