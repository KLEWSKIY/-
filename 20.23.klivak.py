import numpy as np

num_experiments = 100000

samples = np.random.choice(['red', 'blue', 'black'], size=(num_experiments, 3), p=[4/12, 4/12, 4/12])

num_successful_experiments = np.sum(np.sum(samples == 'black', axis=1) >= 2)

probability = num_successful_experiments / num_experiments

print(f"Ймовірність витягнути не менше 2: {probability}")
