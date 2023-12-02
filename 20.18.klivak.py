import numpy as np

num_iterations = 100000

p = 10 / 36

throws = np.random.randint(1, 7, size=(num_iterations, 4))

sums = np.sum(throws, axis=1)

wins = sums <= 9

total_winnings = np.sum(wins * 10)

total_expenses = num_iterations

average_winnings = total_winnings / total_expenses

if average_winnings >= 1/p:
    print("Гра справедлива")
else:
    print("Гра не чесна")
