import numpy as np

# Створіть вектор зі значеннями від 10 до 49
vector = np.arange(10, 50)

# Розверніть вектор (перший елемент стає останнім)
reversed_vector = np.flip(vector)

# Створіть матрицю 3x3 зі значеннями від 0 до 8
matrix = np.arange(9).reshape(3, 3)

# Знайдіть індекси ненульових елементів у списку [1,2,0,0,4,0]
nonzero_indices = np.nonzero([1, 2, 0, 0, 4, 0])

# Створіть одиничну матрицю 3x3
identity_matrix = np.eye(3)

# Створіть масив розміром 3x3x3 з випадковими значеннями
random_3d_array = np.random.rand(3, 3, 3)

# Створіть масив розміром 10x10 з випадковими значеннями і знайдіть мінімальне та максимальне значення
random_10x10_array = np.random.rand(10, 10)
min_value = np.min(random_10x10_array)
max_value = np.max(random_10x10_array)

# Створіть випадковий вектор розміром 30 і знайдіть середнє значення
random_vector = np.random.rand(30)
mean_value = np.mean(random_vector)

# Створіть двовимірний масив з одиницями на межі та нулями всередині
bordered_array = np.ones((5, 5))
bordered_array[1:-1, 1:-1] = 0

# Як додати рамку (з заповненням нулями) навколо існуючого масиву?
existing_array = np.array([[1, 2], [3, 4]])
padded_array = np.pad(existing_array, pad_width=1, mode='constant', constant_values=0)

# Створіть матрицю 5x5 зі значеннями 1,2,3,4 під діагоналлю
diagonal_matrix = np.diag(np.arange(1, 5), k=-1)

# Створіть матрицю 8x8 і заповніть її узором шахової дошки
chessboard = np.zeros((8, 8), dtype=int)
chessboard[1::2, ::2] = 1
chessboard[::2, 1::2] = 1

# Розгляньте масив форми (6,7,8), який індекс (x, y, z) відповідає 100-му елементу?
shape = (6, 7, 8)
index = np.unravel_index(100, shape)

print("1.", vector)
print("2.", reversed_vector)
print("3.", matrix)
print("4.", nonzero_indices)
print("5.", identity_matrix)
print("6.", random_3d_array)
print("7. Мінімальне значення:", min_value, ", Максимальне значення:", max_value)
print("8. Середнє значення:", mean_value)
print("9.", bordered_array)
print("10.", padded_array)
print("11.", diagonal_matrix)
print("12.", chessboard)
print("13. Індекси:", index)
