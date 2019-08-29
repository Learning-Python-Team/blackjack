import random
import sys

HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)


def create_deck():
    """ generate a 6 deck shoe of shuffled cards """
    card_deck = []
    for x in range(6):
        for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
            for rank in range(2, 11):
                card_deck.append((str(rank) + str(suit)))
            for face_cards in ('A', 'J', 'Q', 'K'):
                card_deck.append((str(face_cards) + str(suit)))

    random.shuffle(card_deck)
    return card_deck


def cards_value(cards):
    """ assign values to cards, aces default to 11

    :param cards: cards (rank, suit)
    :return: total value of all cards
    """
    card_value = 0
    aces = 0
    for card in cards:
        if card[0] in ['J', 'Q', 'K']:
            card_value += 10
        elif card[0:2] == '10':
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


def player_action(cards, wager):
    """allows player to hit or stick
    :param wager: bet
    :param cards:player cards
    :return: cards after draw
    """
    # TODO break this into functions by action
    # check if cards are the same and offer split, tested
    try:
        if cards[0][0] == cards[1][0]:
            split = input("Split? (Y)es (N)o").upper()
            # TODO figure out how to process a second player hand with 1 card each
            if split == 'Y':
                split_cards(cards)

    # draw second card on split
    except IndexError:
        cards = draw(cards)

    # checks if first two cards are a natural 21, tested
    if cards_value(cards) == 21:
        # return cards
        return cards, wager

    # checks for 9, 10 , 11 for double down, also checks for aces with default value of 11, tested
    if cards_value(cards) in (9, 10, 11) or (
            cards_value(cards) in (19, 20, 21) and (cards[0][0] == 'A' or cards[1][0] == 'A')):
        # player doubles bet
        double = input("(D)ouble down?").upper()
        if double == 'D':
            wager = int(wager) * 2
            cards = draw(cards)
            return cards, wager

    elif "A" in cards:
        print("ace in double down")

    while True:
        action = input("(H)it, (S)tick").upper()
        if action == "H":
            cards = draw(cards)
            show_hand(cards, dealer_cards, True)
            if cards_value(cards) > 21:
                return cards, wager
        if action == "S":
            break
    # return cards with drawn cards
    return cards, wager


def split_cards(cards):
    """create two hands of cards"""
    # TODO figure out how to process second hand
    player_card_one, player_card_two = cards
    print(player_card_one, player_card_two, "splitting")

    player_one_cards = player_card_one, deck.pop()
    player_two_cards = player_card_two, deck.pop()

    show_hand(player_one_cards, dealer_cards, False)
    show_hand(player_two_cards, dealer_cards, False)

    return player_one_cards


def dealer_action(cards):
    """dealer draws cards"""
    # dealer keeps drawing cards until total value is over 16
    while cards_value(cards) < 16:
        cards = draw(cards)
    # return cards with drawn cards
    return cards


def check_win(wager, cash, total_pot):
    """checks various win conditions

    :param wager: amount of bet
    :param cash: total player money
    :param total_pot: pot carried over from ties
    :return:
    """
    # player has 2 cards totaling 21 player wins 1.5 * bet
    if len(player_cards) == 2 and cards_value(player_cards) == 21:
        cash += int((int(wager) * 1.5)) + total_pot
        total_pot = 0
        print("Player wins with a natural 21\n")
        print("debug", cash, "pot", total_pot)
        return cash, total_pot

    # player loses bet
    elif cards_value(player_cards) > 21:
        show_hand(player_cards, dealer_cards, False)
        cash -= int(wager)
        total_pot = 0
        print("Player busted\n")
        print("debug", cash, "pot", total_pot)
        return cash, total_pot

    # player wins bet
    elif cards_value(dealer_cards) > 21:
        show_hand(player_cards, dealer_cards, False)
        cash += int(wager) + total_pot
        total_pot = 0
        print("Dealer busted\n")
        print("debug", cash, "pot", total_pot)
        return cash, total_pot

    # player loses bet
    elif cards_value(player_cards) < cards_value(dealer_cards):
        show_hand(player_cards, dealer_cards, False)
        cash -= int(wager)
        total_pot = 0
        print("Dealer wins\n")
        print("debug", cash, "pot", total_pot)
        return cash, total_pot

    # bet should be added to pot
    elif cards_value(player_cards) == cards_value(dealer_cards):
        show_hand(player_cards, dealer_cards, False)
        print("Player and dealer tied, pushing bet")
        print("debug", cash, "pot", total_pot)
        cash -= int(wager)
        total_pot = int(wager) * 2
        return cash, total_pot

    # player wins bet
    else:
        show_hand(player_cards, dealer_cards, False)
        cash += int(wager) + total_pot
        total_pot = 0
        print("Player wins\n")
        print("debug", cash)
        return cash, total_pot


if __name__ == '__main__':
    money = 100
    pot = 0
    deck = create_deck()

    while True:
        if money == 0:
            print("You're broke, thanks for playing")
            sys.exit()
        bet = input(f"How much do you want to wager, up to {money}? ")
        print("debug", money)
        # gets first two cards for player and dealer
        player_cards = deck.pop(), deck.pop()
        dealer_cards = deck.pop(), deck.pop()

        while True:
            # display hands
            show_hand(player_cards, dealer_cards, True)
            print()

            # allows player to hit or stick
            player_cards, bet = player_action(player_cards, bet)

            # dealer draws card if total card value is less than 16
            if cards_value(dealer_cards) < 16:
                dealer_cards = dealer_action(dealer_cards)
                break

            if cards_value(dealer_cards) >= 16:
                break

        money, pot = check_win(bet, money, pot)
        print(f"You have {money}, and there's a pot of {pot}")
        """
        again = input("Play again? (Y)es or (N)o").upper()
        if again == "N":
            break
        """
