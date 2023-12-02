import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import imageio.v2 as imageio

def calculate_pi(k):
    n = 2**k
    side_length = 2 * np.sin(np.pi / n)
    perimeter = n * side_length
    approx_pi = perimeter / 2
    return approx_pi

def plot_circle_and_polygon(k):
    n = 2**k
    angle = 2 * np.pi / n
    theta = np.linspace(0, 2*np.pi, 1000)
    x_circle = np.cos(theta)
    y_circle = np.sin(theta)

    side_length = 2 * np.sin(np.pi / n)
    x_polygon = [np.cos(i*angle) for i in range(n+1)]
    y_polygon = [np.sin(i*angle) for i in range(n+1)]

    fig, ax = plt.subplots()
    ax.plot(x_circle, y_circle, label='Circle')
    ax.plot(x_polygon, y_polygon, label=f'{n}-gon')
    ax.legend()
    ax.set_aspect('equal', 'box')
    plt.title(f'Approximation of π using {n}-gon')
    plt.savefig(f'approximation_{k}.png')
    plt.close()

def animate(k):
    plot_circle_and_polygon(k)

k_values = range(2, 10)

for k in k_values:
    animate(k)

# Завантаження зображень
images = [f'approximation_{k}.png' for k in k_values]
frames = [imageio.imread(image) for image in images]

# Запишіть відео
imageio.mimsave('approximation_video.gif', frames, fps=1)
