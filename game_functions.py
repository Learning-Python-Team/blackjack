import random


def create_deck():
    """ generate a 6 deck shoe of shuffled cards """
    card_deck = []
    for x in range(6):
        for suit in ('H', 'S', 'C', 'D'):
            for rank in range(2, 11):
                card_deck.append((str(rank) + str(suit)))
            for face_cards in ('A', 'J', 'Q', 'K'):
                card_deck.append((str(face_cards) + str(suit)))

    random.shuffle(card_deck)
    return card_deck

# for testing
#deck = create_deck()

#print(deck)