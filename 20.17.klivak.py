import numpy as np
import matplotlib.pyplot as plt

num_points = 10000

x = np.random.uniform(-1, 1, num_points)
y = np.random.uniform(0, 1, num_points)

distance = np.sqrt(x**2 + y**2)

inside_circle = distance <= 1

num_inside = np.sum(inside_circle)

pi_approx = 4 * num_inside / num_points

plt.figure(figsize=(8, 8))

circle = plt.Circle((0, 0), 1, alpha=0.5, color='blue')
rectangle = plt.Rectangle((-1, 0), 2, 1, alpha=0.3, color='orange')

plt.gca().add_patch(circle)
plt.gca().add_patch(rectangle)

plt.scatter(x[inside_circle], y[inside_circle], color='green', s=5, label='Inside Circle')
plt.scatter(x[~inside_circle], y[~inside_circle], color='red', s=5, label='Outside Circle')

plt.xlim(-1.1, 1.1)
plt.ylim(-0.1, 1.1)
plt.gca().set_aspect('equal', adjustable='box')
plt.title(f'Approximated π: {pi_approx:.6f}')
plt.legend()

plt.show()

print(f'Approximated π: {pi_approx:.6f}')
