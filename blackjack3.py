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
        elif card[0] == '1' and card[1] == '0':
            card_value += 10
        elif card[0] == 'A':
            aces += 1
        else:
            card_value += int(card[0])

    for ace in range(aces):
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

def player_action(cards):
    """allows player to hit or stick

    :param cards:
    :return: cards after draw
    """
    while True:
        print("(H)it, (S)tick")
        action = input().upper()
        if action == "H":
            cards = draw(cards)
            show_hand(cards, dealer_cards, True)
            if cards_value(cards) > 21:
                return cards
        if action == "S":
            break
    return cards


def dealer_action(cards):
    pass


deck = create_deck()

while True:
    # gets first two cards for player and dealer
    player_cards = deck.pop(), deck.pop()
    dealer_cards = deck.pop(), deck.pop()

    while True:
        # display hands
        show_hand(player_cards, dealer_cards, True)

        # allows player to hit or stick
        player_cards = player_action(player_cards)
        # exit loop if busted on hits
        if cards_value(player_cards) > 21:
            print("Busted")
            print()
            break
        else:
            dealer_action(dealer_cards

    again = input("Play again? (Y)es or (N)o").upper()
    if again != "Y":
        break
