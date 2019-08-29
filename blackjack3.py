import random
import sys
# import pysnooper

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
    """ draws a single card and adds it to hand

    :param cards:
    :return: cards + one card
    """
    cards += (deck.pop(),)
    return cards

#@pysnooper.snoop()
def player_action(cards, wager, cash):
    """allows player to hit or stick
    :param cash:
    :param wager: bet
    :param cards:player cards
    :return: cards after draw
    """

    if cards_value(cards) == 21:
        return cards, wager

    # checks for 9, 10 , 11 for double down, also checks for aces with default value of 11
    if cards_value(cards) in (9, 10, 11) or (
            cards_value(cards) in (19, 20, 21) and (cards[0][0] == 'A' or cards[1][0] == 'A')):
        double = input("(D)ouble down?").upper()
        if double == 'D':
            if wager * 2 <= cash:
                wager = int(wager) * 2
                cards = draw(cards)
                return cards, wager
            else:
                return cards, wager
    cards, wager = hit_stick(cards, wager)
    return cards, wager


def hit_stick(cards, wager):
    while True:
        action = input("(H)it, (S)tick").upper()
        if action == "H":
            cards = draw(cards)
            show_hand(cards, dealer_cards, True)
            if cards_value(cards) > 21:
                return cards, wager
        if action == "S":
            break
    return cards, wager


def dealer_action(cards):
    """dealer keeps drawing cards until total value is over 16

    :param cards:
    :return: dealer hand
    """
    while cards_value(cards) < 16:
        cards = draw(cards)
    return cards


def check_win(wager, cash, total_pot, player_crds, dealer_crds):
    """ checks various win conditions
    
    :param wager: amount of bet
    :param cash: total player money
    :param total_pot: pot from pushing
    :param player_crds: 
    :param dealer_crds: 
    :return: 
    """
    # player has 2 cards totaling 21 player wins 1.5 * bet
    if len(player_crds) == 2 and cards_value(player_crds) == 21:
        cash += int((int(wager) * 1.5)) + total_pot
        total_pot = 0
        print("Player wins with a natural 21\n")
        return cash, total_pot

    # player loses bet
    elif cards_value(player_crds) > 21:
        show_hand(player_crds, dealer_crds, False)
        cash -= int(wager)
        total_pot = 0
        print("Player busted\n")
        return cash, total_pot

    # player wins bet
    elif cards_value(dealer_crds) > 21:
        show_hand(player_crds, dealer_crds, False)
        cash += int(wager) + total_pot
        total_pot = 0
        print("Dealer busted\n")
        return cash, total_pot

    # player loses bet
    elif cards_value(player_crds) < cards_value(dealer_crds):
        show_hand(player_crds, dealer_crds, False)
        cash -= int(wager)
        total_pot = 0
        print("Dealer wins\n")
        return cash, total_pot

    # bet should be added to pot
    elif cards_value(player_crds) == cards_value(dealer_crds):
        show_hand(player_crds, dealer_crds, False)
        print("Player and dealer tied, pushing bet")
        cash -= int(wager)
        total_pot = int(wager) * 2
        return cash, total_pot

    # player wins bet
    else:
        show_hand(player_crds, dealer_crds, False)
        cash += int(wager) + total_pot
        total_pot = 0
        print("Player wins\n")
        return cash, total_pot


def get_bet(cash):
    while True:
        wager = input(f"How much do you want to wager, up to {cash}? Or (Q)uit").upper()
        if wager == "Q":
            print("Thanks for playing")
            sys.exit()
        if not wager.isdigit():
            continue
        wager = int(wager)
        if wager <= cash:
            return wager


# @pysnooper.snoop()
def split_cards(cards, wager, cash, pot, dealer_cards):
    # Draw second card for each half of split
    hand1 = (cards[0],deck.pop(), )
    hand2 = (cards[1],deck.pop(), )

    # process hand 1
    print("Hand1")
    show_hand(hand1, dealer_cards, True)
    hand1, wager = hit_stick(hand1, wager)
    dealer_cards = dealer_action(dealer_cards)
    show_hand(hand1, dealer_cards, False)
    cash, pot = check_win(wager, cash, pot, hand1, dealer_cards)

    print("Hand2")
    show_hand(hand2, dealer_cards, False)
    hand2, wager = hit_stick(hand2, wager)
    show_hand(hand2, dealer_cards, False)
    cash, pot = check_win(wager, cash, pot, hand2, dealer_cards)

    return cash, pot


if __name__ == '__main__':
    money = 100
    pot = 0
    deck = create_deck()

    while True:
        if money == 0:
            print("You're broke, thanks for playing")
            sys.exit()

        bet = get_bet(money)

        # gets first two cards for player and dealer

        player_cards = deck.pop(), deck.pop()
        # player_cards = ('9♠', '9♦')  # for testing splits

        dealer_cards = deck.pop(), deck.pop()

        while True:
            # display hands
            show_hand(player_cards, dealer_cards, True)
            print()

            # if cards match offer split
            if player_cards[0][0] == player_cards[1][0]:
                split = input("(S)plit?").upper()
                if split == 'S':
                    money, pot = split_cards(player_cards, bet, money, pot, dealer_cards)
                    break

            else:
                # allows player to hit or stick
                player_cards, bet = player_action(player_cards, bet, money)

                # dealer draws card if total card value is less than 16
                dealer_cards = dealer_action(dealer_cards)

                # payout
                money, pot = check_win(bet, money, pot, player_cards, dealer_cards)
                break

        print(f"You have {money}, and there's a pot of {pot}")

