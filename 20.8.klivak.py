import numpy as np

def transform_vector(vector):
    negative_values = vector[vector < 0]
    positive_values = vector[vector >= 0]

    return np.concatenate((negative_values, positive_values))


initial_vector = np.array([3, -1, 4, -2, 0, 5, -6, 7])
transformed_vector = transform_vector(initial_vector)

print("Початковий вектор:", initial_vector)
print("Кінцевий вектор:", transformed_vector)
