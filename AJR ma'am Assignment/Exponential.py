import numpy as np
import matplotlib.pyplot as plt

def exponential(lembda,x):
  prob = lembda*exp(-lembda*x)
  return prob


if __name__ == "__main__":
  obs = int(input("Enter Number of Observation : "))

  probs = []


  x = np.linspace(0,50,obs)
  lembda = 1/np.mean(x)

  for i in x:
    probability = exponential(lembda,i)
    probs.append(probability)
  
  plt.plot(x,probs,color="blue")
  plt.xlabel("Data Points")
  plt.ylabel("Probability Distribution Function")
  plt.title("Exponential Distribution")
  plt.show()