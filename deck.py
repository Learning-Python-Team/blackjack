import random

# TODO turn this into class Deck

HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)


def create_deck():
    """generates a deck of cards (rank_suit)"""
    card_deck = []
    # create a 6 deck shoe
    for x in range(6):
        # for each suit
        for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
            # create normal cards
            for rank in range(2, 11):
                card_deck.append((str(rank) + str(suit)))
            # create face cards
            for face_cards in ('A', 'J', 'Q', 'K'):
                card_deck.append((str(face_cards) + str(suit)))

    random.shuffle(card_deck)
    return card_deck


def cards_value(cards):
    """covert all cards to value adjusting for aces"""
    card_value = 0
    aces = 0
    for card in cards:
        # convert face cards to 10
        if card[0] in ['J', 'Q', 'K']:
            card_value += 10
        # hack for 10 to allow for the extra character
        elif card[0:2] == '10':
            card_value += 10
        # count aces
        elif card[0] == 'A':
            aces += 1
        # assign regular cards values
        else:
            card_value += int(card[0])

    for ace in range(aces):
        # aces are 11 unless it pushed total over 21
        if card_value + 11 <= 21:
            card_value += 11
        else:
            card_value += 1

    return card_value


def show_hand(player, dealer, hide_dealer):
    """function to display cards, if dealer false hide one card

    :param player: player cards
    :param dealer: dealer cards
    :param hide_dealer: hide a card or not
    :return:
    """
    if hide_dealer:
        print("Dealer's Hand")
        print("XX " + dealer[0], end=" ")
        print()
    else:
        print("Dealer's Hand")
        for card in dealer:
            print(card, end=" ")
        print()
    print("Player's Hand")
    for card in player:
        print(card, end=" ")
    print()


def draw(cards):
    cards += (deck.pop(),)
    return cards

"""
# for testing
deck = create_deck()
player_cards = deck.pop(), deck.pop()
dealer_cards = deck.pop(), deck.pop()

player_value = cards_value(player_cards)
dealer_value = cards_value(dealer_cards)
print(player_cards, player_value)
print(dealer_cards, dealer_value)


# does not update value

player_cards = draw(player_cards)
show_hand(player_cards, dealer_cards, True)

player_cards = draw(player_cards)
show_hand(player_cards, dealer_cards, True)
"""