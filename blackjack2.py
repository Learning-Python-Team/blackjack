# TODO player total 21 isnt automatic blackjack
# TODO double down, split cards draw one card for each
# TODO add money
# TODO add betting
# TODO dealer hand should be a function looping to draw more cards
# TODO if player sticks should check if dealers hand is greater BEFORE dealer draws card

import random
import sys

# initialize deck
# TODO better way to create deck
deck = ['A', 'A', 'A', 'A', 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7,
        8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 'J', 'J', 'J', 'J',
        'Q', 'Q', 'Q', 'Q', 'K', 'K', 'K', 'K']


def draw_card():
    """draw random card"""
    card = random.choice(deck)
    deck.remove(card)
    return card


def card_value(card):
    """covert card to value"""
    if card in ['J', 'Q', 'K']:
        card = 10
    if card == 'A':
        # TODO im not sure this works
        try:
            choice = int(input('Ace, 1 or 11?'))
        except ValueError:
            card = 1
            return card

        if choice == 1:
            card = 1
        else:
            card = 11
    return card


def dealer_card_value(card):
    """dealer card conversion"""
    if card in ['J', 'Q', 'K']:
        card = 10
    if card == 'A':
        card = 11
    return card


def check_cards():
    if player_hand == 21:
        print("BLACKJACK, player wins (check_cards)")

    elif player_hand > 21:
        print("Player Busted (check_cards)")


def place_bet(money):
    """place bet up to max on money"""
    # TODO Place and calculate bet return bet
    pass


# add starting money
money = 100

while True:
    # draw player cards
    pc1 = draw_card()
    pc2 = draw_card()

    # draw dealer cards
    dc1 = draw_card()
    dc2 = draw_card()
    # TODO place_bet function
    bet = place_bet(money)
    print(f"\nPlayers hand {pc1} {pc2} Dealer showing a {dc1}\n")

    # convert values
    player_card1 = card_value(pc1)
    player_card2 = card_value(pc2)

    # assign dealer card values
    dealer_card1 = dealer_card_value(dc1)
    dealer_card2 = dealer_card_value(dc2)
    dealer_hand = dealer_card1 + dealer_card2

    # show player cards
    player_hand = player_card1 + player_card2
    print(f"Player cards: {pc1} {pc2} = {player_hand}")

    if player_hand == 21:
        print("BLACKJACK, player wins")
        continue

    # hit or stick
    print("Hit or Stick 'h' or 's' > ", end="")
    hit_or_stick = input()

    if hit_or_stick.lower() == 's':
        check_cards()
    else:
        pc3 = draw_card()
        player_card3 = card_value(pc3)
        player_hand += player_card3
        print(f"Player cards: {pc1} {pc2} {pc3} = {player_hand}")
        check_cards()
        # TODO this should be in a function
        if player_hand < 21:

            # hit or stick
            print("Hit or Stick 'h' or 's' > ", end="")
            hit_or_stick = input()

            if hit_or_stick.lower() == 's':
                check_cards()
            else:
                pc4 = draw_card()
                player_card4 = card_value(pc4)
                player_hand += player_card4
                print(f"Player cards: {pc1} {pc2} {pc3} {pc4} = {player_hand}")
                check_cards()

                if player_hand < 21:
                    # hit or stick
                    print("Hit or Stick 'h' or 's' > ", end="")
                    hit_or_stick = input()
                    if hit_or_stick.lower() == 's':
                        check_cards()
                    else:
                        pc5 = draw_card()
                        player_card5 = card_value(pc5)
                        player_hand += player_card5
                        print(f"Player cards: {pc1} {pc2} {pc3} {pc4} {pc5}= {player_hand}")
                        check_cards()

    # show dealer cards
    print(f"Dealers hand {dc1} {dc2} = {dealer_hand}")

    # dealer draw cards
    if dealer_hand < 16:
        dc3 = draw_card()
        dealer_card3 = dealer_card_value(dc3)
        dealer_hand += dealer_card3
        if dealer_hand > 21:
            print(f"Dealers bust! {dc1} {dc2} {dc3} Player wins")
        else:
            print(f"Dealers hand {dc1} {dc2} {dc3} = {dealer_hand}")

        if dealer_hand < 16:
            dc4 = draw_card()
            dealer_card4 = dealer_card_value(dc4)
            dealer_hand += dealer_card4
            if dealer_hand > 21:
                print(f"Dealers bust! {dc1} {dc2} {dc3} {dc4} = {dealer_hand} Player wins")
                continue
            else:
                print(f"Dealers hand {dc1} {dc2} {dc3} {dc4} = {dealer_hand}")

            if dealer_hand < 16:
                dc5 = draw_card()
                dealer_card5 = dealer_card_value(dc5)
                dealer_hand += dealer_card5
                if dealer_hand > 21:
                    print(f"Dealers bust! {dc1} {dc2} {dc3} {dc4} {dc5} Player wins")
                    continue
                else:
                    print(f"Dealers hand {dc1} {dc2} {dc3} {dc4} {dc5} = {dealer_hand}")

    if dealer_hand >= player_hand or player_hand > 21:
        print("Dealer wins (while_loop)")
        # TODO money - bet
    else:
        print("Player wins (while_loop)")
        # TODO money + bet


    play = input("Play again?  y/n: ").lower()
    if play == 'n':
        break
