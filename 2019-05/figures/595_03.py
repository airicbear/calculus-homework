import numpy as np
import matplotlib.pyplot as plt

def f(x):
    if x == 2:
        return -3
    return 5 - x

x = [1, 1.98, 2, 2.02, 3]
y = [f(i) for i in x]

plt.plot(x[:2], y[:2], c="black")
plt.plot(x[3:], y[3:], c="black")
plt.scatter(x[2], y[2], c="black")
plt.grid()

plt.savefig('595_03')
plt.show()

