import numpy as np

def play_round(p, capital):
    return np.random.rand() < p

def simulate_game(K, p):
    capital = K
    rounds = 0

    while capital > 0:
        if play_round(p, capital):
            return rounds
        else:
            capital -= 1
            rounds += 1

    return rounds

def monte_carlo_simulation(K, p, num_simulations):
    results = []

    for _ in range(num_simulations):
        results.append(simulate_game(K, p))

    probability_of_losing = len([r for r in results if r > 0]) / num_simulations
    return probability_of_losing

K = 10
p = 0.3
num_simulations = 100000

probability_of_losing = monte_carlo_simulation(K, p, num_simulations)
print(f"Ймовірність втратити всі гроші: {probability_of_losing}")
