from math import exp
import matplotlib.pyplot as plt
import numpy as np

def fact(x):
    if x==0:
        return 1
    else:
        return (x * fact(x-1))

def poisson(x,lembda):
    prob = exp(-lembda)*lembda**x/fact(x)
    return prob

if __name__ == "__main__" :
    
    obs = int(input("Enter No. od observation (< 172) : "))

    probs = []

    x = np.linspace(0,obs-1,obs)
    print(x)
    lembda = np.mean(x)
    
    for i in range(obs):
        probbability = poisson(i,lembda)
        probs.append(probbability)

plt.plot(x,probs,color="red")
plt.xlabel("Data Points")
plt.ylabel("Probability Mass Function")
plt.title("Poisson Distribution")
plt.show()

print(probs)