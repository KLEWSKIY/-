import random

class Decks:
    def __init__(self):
        self.deck = [i for i in range(7, 15)] * 4

    def deal(self):
        random.shuffle(self.deck)
        hands = [self.deck[i:i+10] for i in range(0, len(self.deck), 10)]
        pickup = self.deck[-2:]
        return hands, pickup

def check_guaranteed_win(hand):
    if max(hand) >= 14:
        return True
    if len([card for card in hand if card >= 11]) >= 4:
        return True
    if len([card for card in hand if card >= 10]) >= 5:
        return True
    if len(set(hand)) >= 8:
        return True
    return False

total_hands = 100000

wins_a = 0
for _ in range(total_hands):
    decks = Decks()
    hands, _ = decks.deal()
    if any(check_guaranteed_win(hand) for hand in hands):
        wins_a += 1

probability_a = wins_a / total_hands
print(f"Ймовірність без урахування прикупу: {probability_a}")

wins_b = 0
for _ in range(total_hands):
    decks = Decks()
    hands, pickup = decks.deal()
    if any(check_guaranteed_win(hand + pickup) for hand in hands):
        wins_b += 1

probability_b = wins_b / total_hands
print(f"Ймовірність з урахуванням прикупу: {probability_b}")




