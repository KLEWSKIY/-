# numpy as np / matplotlib as plt
# ((n + np.sum([n / 3**i for i in range(1, n+1)])) * (n - 3)**n * np.sqrt(n)) / (2 * n**2 + 5)
#
import numpy as np
import matplotlib.pyplot as plt

def calculate_an(n):
    return ((n + np.sum([n / 3**i for i in range(1, n+1)])) * (n - 3)**n * np.sqrt(n)) / (2 * n**2 + 5)

n_values = np.arange(1, 1001)
an_values = [calculate_an(n) for n in n_values]

b = an_values[-1]

epsilon = 0.1

plt.plot(n_values, an_values, label='a_n', color='b')
plt.axhline(y=b, color='r', linestyle='--', label='y = b')

plt.fill_between(n_values, b - epsilon, b + epsilon, alpha=0.2, color='g', label=f'b ± ε ({b - epsilon}, {b + epsilon})')

plt.xlabel('n')
plt.ylabel('a_n')
plt.legend()
plt.grid()

plt.show()
