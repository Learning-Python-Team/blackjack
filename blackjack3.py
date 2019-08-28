import random

HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)


def create_deck():
    """generates a deck of cards (rank_suit)"""
    # TODO maka a 6 deck shoe
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
    :return: cards after draw, natural: T/F
    """
    # TODO break this into functions by action
    print("debug", cards)
    # check if cards are the same and offer split, tested
    if cards[0][0] == cards[1][0]:
        print("Split? (Y)es (N)o")
        split = input().upper()
        # TODO figure out how to process a second player hand with 1 card each
        if split == 'Y':
            player_card_one, player_card_two = cards
            print(player_card_one, player_card_two, "splitting")

    # checks if first two cards are a natural 21, tested
    if cards_value(cards) == 21:
        # return cards
        return cards

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
    # return cards, natural
    return cards


def dealer_action(cards):
    """dealer draws cards"""
    show_hand(player_cards, cards, False)
    # dealer keeps drawing cards until total value is over 16
    while cards_value(cards) < 16:
        cards = draw(cards)
        show_hand(player_cards, cards, False)

    return cards


deck = create_deck()

while True:
    # gets first two cards for player and dealer
    player_cards = deck.pop(), deck.pop()
    dealer_cards = deck.pop(), deck.pop()

    while True:
        # display hands
        show_hand(player_cards, dealer_cards, True)
        print()

        # allows player to hit or stick
        player_cards = player_action(player_cards)

        # dealer draws card if total card value is less than 16
        if cards_value(dealer_cards) < 16:
            dealer_cards = dealer_action(dealer_cards)
            break

        if cards_value(dealer_cards) >= 16:
            break

    if len(player_cards) == 2 and cards_value(player_cards) == 21:
        # player wins 1.5 * bet
        print("Player wins with a natural 21\n")

    elif cards_value(player_cards) > 21:
        print("Player busted\n")

    elif cards_value(dealer_cards) > 21:
        print("Dealer busted\n")

    elif cards_value(player_cards) < cards_value(dealer_cards):
        print("Dealer wins\n")

    elif cards_value(player_cards) == cards_value(dealer_cards):
        # bet should be added to pot
        print("Player and dealer tied, pushing bet")

    else:
        show_hand(player_cards, dealer_cards, False)
        print("Player wins\n")

    again = input("Play again? (Y)es or (N)o").upper()
    if again == "N":
        break
