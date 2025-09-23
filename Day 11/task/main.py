def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return cards

user_cards = []
computer_cards = []
for _ in range(2):
    new_cards = deal_card()
    user_cards.append(new_cards)
    computer_cards.append(new_cards)

def calculate_score(cards):
    if 11 in cards and 10 in cards and len(cards) == 2:
        return 0
    return sum(cards)
