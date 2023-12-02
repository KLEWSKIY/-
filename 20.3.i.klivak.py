import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def f(x):
    return 1 / (1 + x + 1e-8) ** 2

def taylor_term(n, x):
    return (-1) ** n * (n + 1) * x ** n

a, b = -1, 1
m = 10

x_values = np.linspace(a, b, 1000)
y_values = f(x_values)


plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label='f(x)')

def animate(n):
    plt.clf()
    plt.plot(x_values, y_values, label='f(x)')

    approximation = np.zeros_like(x_values)
    for i in range(n + 1):
        approximation += taylor_term(i, x_values)

    plt.plot(x_values, approximation, label=f'Taylor (n={n})')
    plt.legend()

anm = FuncAnimation(plt.gcf(), animate, frames=range(m + 1), repeat=False)

anm.save('taylor_approximation.gif', writer='pillow')

plt.show()
