import numpy as np

def normalize_matrix(matrix):
    normalized_matrix = (matrix - np.mean(matrix)) / np.std(matrix)
    return normalized_matrix

def test_normalize_matrix():
    matrix = np.random.rand(5, 5)
    normalized_matrix = normalize_matrix(matrix)
    assert np.isclose(np.mean(normalized_matrix), 0) and np.isclose(np.std(normalized_matrix), 1)
    print("Тест normalize_matrix пройдено успішно!")

def find_common_values(array1, array2):
    common_values = np.intersect1d(array1, array2)
    return common_values

def test_find_common_values():
    array1 = np.array([1, 2, 3, 4, 5])
    array2 = np.array([4, 5, 6, 7, 8])
    common_values = find_common_values(array1, array2)
    assert np.array_equal(common_values, np.array([4, 5]))
    print("Тест find_common_values пройдено успішно!")

def create_matrix():
    matrix = np.tile(np.arange(5), (5, 1))
    return matrix

def test_create_matrix():
    matrix = create_matrix()
    assert np.array_equal(matrix, np.array([[0, 1, 2, 3, 4]]*5))
    print("Тест create_matrix пройдено успішно!")

def number_generator():
    for _ in range(10):
        yield np.random.randint(0, 100)

def test_number_generator():
    gen = number_generator()
    generated_numbers = [next(gen) for _ in range(10)]
    assert len(generated_numbers) == 10
    print("Тест number_generator пройдено успішно!")

def generate_and_sort_vector():
    random_vector = np.random.randint(0, 100, 10)
    sorted_vector = np.sort(random_vector)
    return sorted_vector

def test_generate_and_sort_vector():
    vector = generate_and_sort_vector()
    assert np.array_equal(vector, np.sort(vector))
    print("Тест generate_and_sort_vector пройдено успішно!")

def check_arrays_equality(array1, array2):
    return np.array_equal(array1, array2)

def test_check_arrays_equality():
    array1 = np.array([1, 2, 3])
    array2 = np.array([1, 2, 3])
    assert check_arrays_equality(array1, array2)
    print("Тест check_arrays_equality пройдено успішно!")

# Виклик усіх тестів
test_normalize_matrix()
test_find_common_values()
test_create_matrix()
test_number_generator()
test_generate_and_sort_vector()
test_check_arrays_equality()





