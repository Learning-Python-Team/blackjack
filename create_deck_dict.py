def create_deck():
    """ generate a 6 deck shoe of shuffled cards """
    card_deck = []

    for suit in ('H', 'S', 'C', 'D'):
        for rank in range(2, 11):
            card_deck.append((str(rank) + str(suit)))
        for face_cards in ('A', 'J', 'Q', 'K'):
            card_deck.append((str(face_cards) + str(suit)))
    return card_deck

card_deck = create_deck()

card_dict = {}

for card in card_deck:
    card_dict[card] = "images/" + card + '.png'

print(card_dict)