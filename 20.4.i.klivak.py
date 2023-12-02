import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 1 / (1 + x)**2

def approx_series(x, m):
    series_sum = 0
    for i in range(m):
        series_sum += (-1)**i * (i + 1) * x**i
    return series_sum

a = -1
b = 1
m = 5

x_vals = np.linspace(a, b, 1000)
f_vals = f(x_vals)
approx_vals = approx_series(x_vals, m)

g_vals = np.abs(f_vals - approx_vals)

plt.figure(figsize=(10, 6))
plt.plot(x_vals, f_vals, label='f(x)')
plt.plot(x_vals, approx_vals, label=f'Approximation (m={m})')
plt.fill_between(x_vals, f_vals, approx_vals, where=(f_vals > approx_vals), color='lightcoral')
plt.fill_between(x_vals, f_vals, approx_vals, where=(f_vals < approx_vals), color='lightblue')
plt.legend()

plt.figure(figsize=(10, 6))
plt.plot(x_vals, g_vals, label='g(x)')
plt.fill_between(x_vals, 0, g_vals, color='lightgreen')
plt.legend()

rect_area = (b - a) * max(max(f_vals), max(approx_vals))
error_area = np.trapz(g_vals, x=x_vals)
mean_error = np.sqrt(error_area / rect_area)

print(f'Похибка: {mean_error}')

plt.show()
