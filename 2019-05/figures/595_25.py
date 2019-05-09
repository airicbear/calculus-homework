import numpy as np
import matplotlib.pyplot as plt

# Plot the function
f = lambda x: x ** 3 - 3 * x + 1
xp = np.linspace(-2, 2, 100)
plt.plot(xp, f(xp))
plt.xlabel('x')
plt.ylabel('f(x)')

# Plot extrema and points of inflection
x = np.array([-1, 0, 1])
y = np.array([f(i) for i in x])
plt.scatter(x, y)
for i in x:
    plt.annotate('({}, {})'.format(i, f(i)), [i, f(i)])

plt.savefig('595_25')
plt.show()

