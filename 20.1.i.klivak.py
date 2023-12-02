import numpy as np
import matplotlib.pyplot as plt

def a_n(n):
    numerator = 5 * n**2 + 7 * n + 1
    denominator = 5 * n**2 + 3 * n + 6
    return np.power(numerator / denominator, n - 3)

# Задане значення b
b = np.power((5 * 10**6 + 7 * 10**3 + 1) / (5 * 10**6 + 3 * 10**3 + 6), 10**6 - 3)

# Генеруємо масив n
n_values = np.arange(1, 101, 1)

# Обчислюємо a_n для кожного значення n
a_n_values = a_n(n_values)

# Побудова графіка a_n
plt.figure(figsize=(10, 6))
plt.plot(n_values, a_n_values, label='a_n')
plt.axhline(y=b, color='r', linestyle='--', label='b')
plt.xlabel('n')
plt.ylabel('a_n')
plt.title('Графік послідовності a_n та горизонтальна пряма y=b')
plt.legend()
plt.grid(True)

# Перевірка умови для всіх n > k
epsilon = 0.1
k = 50
condition_met = np.all(np.abs(a_n_values[k:] - b) < epsilon)

if condition_met:
    print(f'Умова |a_n - b| < epsilon виконується для всіх n > {k}')
else:
    print(f'Умова |a_n - b| < epsilon не виконується для всіх n > {k}')

# Побудова смуги
plt.figure(figsize=(10, 6))
plt.plot(n_values, a_n_values, label='a_n')
plt.axhline(y=b, color='r', linestyle='--', label='b')
plt.fill_between(n_values, b - epsilon, b + epsilon, color='gray', alpha=0.5, label='Смуга (b - ε, b + ε)')
plt.xlabel('n')
plt.ylabel('a_n')
plt.title('Графік послідовності a_n, горизонтальна пряма y=b та смуга (b - ε, b + ε)')
plt.legend()
plt.grid(True)

plt.show()
