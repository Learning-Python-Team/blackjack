import random

# TODO turn this into class Deck

HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)


def deck():
    """generates a deck of cards as a tuple (suit, rank)"""
    card_deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            card_deck.append((rank, str(suit)))
        for face_cards in ('A', 'J', 'Q', 'K'):
            card_deck.append((face_cards, str(suit)))
    random.shuffle(card_deck)
    return card_deck


deck = deck()

print(deck)
