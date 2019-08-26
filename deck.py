import random

# TODO turn this into class Deck

HEARTS   = chr(9829)
DIAMONDS = chr(9830)
SPADES   = chr(9824)
CLUBS    = chr(9827)


def deck():
    """generates a deck of cards as a tuple (suit, rank)"""
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(suit), rank))
        for face_card in ('A', 'J', 'Q', 'K'):
            deck.append((str(suit), face_card))
    random.shuffle(deck)
    return deck

print(deck())



