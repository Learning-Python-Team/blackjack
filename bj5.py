import pygame
from pygame.locals import *
import random
import sys

# Card object
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.rank}{self.suit}'


# Deck object
class Deck:
    def __init__(self):
        # Adds cards into deck with suits and number on them.
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        s = ''
        for i in range(len(self.deck)):
            s += str(self.deck[i]) + '\n'
        return s

    def shuffle(self):
        random.shuffle(self.deck)

    # Deals a card by removing a card from the Deck.
    def deal(self):
        is_empty = False
        if len(self.deck) == 0:
            is_empty = True
        if is_empty is False:
            return self.deck.pop()


# Hand object
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    # Adds a card to the hand and adjust for aces if value is above 21
    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'A':
            self.aces += 1
        if self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


# These are values used to create the cards and color scheme respectively.
suits = ('D', 'H', 'S', 'C')
ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}


# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (14, 130, 43)
RED = (255, 0, 0)


def play():
    pygame.init()
    window_x = 1200
    window_y = 600
    game_window = pygame.display.set_mode((window_x, window_y))
    pygame.display.set_caption("Blackjack")

    # create play button rect
    play_button = pygame.image.load('images/play.png')
    play_rect = play_button.get_rect()
    play_rect.topleft = (475, 250)

    # draw screen and add objects
    game_window.fill(GREEN)
    game_window.blit(play_button, (475, 250))

    pygame.display.update()

    # get events
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if play_rect.collidepoint(event.pos):
                    player = Hand()
                    dealer = Hand()
                    deck = Deck()
                    take_bet(100, player, dealer, deck)

def take_bet(bet, player, dealer, deck):
    window_x = 1200
    window_y = 600
    game_window = pygame.display.set_mode((window_x, window_y))
    pygame.display.set_caption("Blackjack Place your Bet")
    game_window.fill(GREEN)
    pygame.display.update()

    # get events
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

if __name__ == '__main__':
    play()