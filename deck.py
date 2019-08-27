import random

# TODO turn this into class Deck

HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)


def create_deck():
    """generates a deck of cards (rank_suit)"""
    card_deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            card_deck.append((str(rank) + str(suit)))
        for face_cards in ('A', 'J', 'Q', 'K'):
            card_deck.append((str(face_cards) + str(suit)))
    random.shuffle(card_deck)
    return card_deck


def cards_value(cards):
    """covert all cards to value adjusting for aces"""
    card_value = 0
    aces = 0
    for card in cards:
        if card[0] in ['J', 'Q', 'K']:
            card_value += 10
            print("adding 10")
        elif card[0] == '1' and card[1] == '0':
            card_value += 10
            print("adding 10")
        elif card[0] == 'A':
            aces += 1
        else:
            card_value += int(card[0])
            print("adding", int(card[0]))

    for ace in range(aces):
        if card_value + 11 <= 21:
            card_value += 11
            (print('adding 11'))
        else:
            card_value += 1
            print("adding 1")
    return card_value


# for testing
deck = deck()
cards = deck.pop(), deck.pop(), deck.pop()
# print(deck)
for i in range(10):
    cards = deck.pop(), deck.pop(), deck.pop()
    for card in cards:
        print(card, end=" ")
    print()
    print(cards_value(cards))
