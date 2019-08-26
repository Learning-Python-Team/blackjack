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
            card_deck.append((str(suit), rank))
        for face_card in ('A', 'J', 'Q', 'K'):
            card_deck.append((str(suit), face_card))
    random.shuffle(card_deck)
    return card_deck


print(deck())
