import pygame
from pygame.locals import *
import random
import sys
import pysnooper

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

pygame.init()
# Used to manage how fast the screen updates
clock = pygame.time.Clock()


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (14, 130, 43)
RED = (255, 0, 0)


# Used to add text to the game when needed.
def add_text(text, font, surface, x, y, color):
    textobject = font.render(text, 1, color)
    textrect = textobject.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobject, textrect)

def play():

    window_x = 1200
    window_y = 600
    game_window = pygame.display.set_mode((window_x, window_y))
    pygame.display.set_caption("Blackjack")

    # create play button rect
    play_button = pygame.image.load('images/play.png')
    play_rect = play_button.get_rect()
    play_rect.topleft = (475, 100)

    # draw screen and add objects
    game_window.fill(GREEN)
    game_window.blit(play_button, (475, 50))

    pygame.display.update()
    clock.tick()

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


def take_bet(chips, player, dealer, deck):

    window_x = 1200
    window_y = 600
    game_window = pygame.display.set_mode((window_x, window_y))

    if chips < 5:
        game_over()
    bets_placed = False

    pygame.display.set_caption("Blackjack Place your Bet")
    game_window.fill(GREEN)

    # text setting
    font_obj = pygame.font.Font('freesansbold.ttf', 40)
    text_surface_obj = font_obj.render("Place your bet", True, BLACK, GREEN)
    text_rect_obj = text_surface_obj.get_rect()
    text_rect_obj.center = (window_x * .5, window_y * .050)

    # text setting
    font_obj1 = pygame.font.Font('freesansbold.ttf', 32)
    text_surface_obj1 = font_obj1.render("CHIPS " + str(chips), True, BLACK, GREEN)
    text_rect_obj1 = text_surface_obj1.get_rect()
    text_rect_obj1.center = (window_x * .5, window_y * .150)

    # draw text to screen
    game_window.blit(text_surface_obj, text_rect_obj)
    game_window.blit(text_surface_obj1, text_rect_obj1)

    # bet 5 button
    bet_5_pos = (100, 300)
    bet_5 = pygame.image.load('images/5.png')
    bet_5_rect = bet_5.get_rect()
    bet_5_rect.topleft = (bet_5_pos)

    # bet 10 button
    bet_10_pos = (300, 150)
    bet_10 = pygame.image.load('images/10.png')
    bet_10_rect = bet_10.get_rect()
    bet_10_rect.topleft = (bet_10_pos)

    # bet 25 button
    bet_25_pos = (500, 300)
    bet_25 = pygame.image.load('images/25.png')
    bet_25_rect = bet_25.get_rect()
    bet_25_rect.topleft = (bet_25_pos)

    # bet 5 button
    bet_50_pos = (700, 150)
    bet_50 = pygame.image.load('images/50.png')
    bet_50_rect = bet_50.get_rect()
    bet_50_rect.topleft = (bet_50_pos)

    # bet 5 button
    bet_100_pos = (900, 300)
    bet_100 = pygame.image.load('images/100.png')
    bet_100_rect = bet_100.get_rect()
    bet_100_rect.topleft = (bet_100_pos)

    # draw chip buttons on screen
    game_window.blit(bet_5, bet_5_rect)
    game_window.blit(bet_10, bet_10_rect)
    game_window.blit(bet_25, bet_25_rect)
    game_window.blit(bet_50, bet_50_rect)
    game_window.blit(bet_100, bet_100_rect)

    pygame.display.update()
    clock.tick()

    # get events
    while bets_placed == False:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if bet_5_rect.collidepoint(event.pos):
                    if chips >= 5:
                        bet = 5
                        bets_placed = True
                if bet_10_rect.collidepoint(event.pos):
                    if chips >= 10:
                        bet = 10
                        bets_placed = True
                if bet_25_rect.collidepoint(event.pos):
                    if chips >= 25:
                        bet = 25
                        bets_placed = True
                if bet_50_rect.collidepoint(event.pos):
                    if chips >= 50:
                        bet = 50
                        bets_placed = True
                if bet_100_rect.collidepoint(event.pos):
                    if chips >= 100:
                        bet = 100
                        bets_placed = True

    while bets_placed is True:
        deck = Deck()
        deck.shuffle()
        player.add_card(deck.deal())
        player.add_card(deck.deal())
        dealer.add_card(deck.deal())
        dealer.add_card(deck.deal())
        award = play_hand(bet, chips, player, dealer, deck)
        chips += award
        pygame.display.update()
        take_bet(chips, player, dealer, deck)


def play_hand(bet, chips, player, dealer, deck):
    window_x = 1200
    window_y = 600
    game_window = pygame.display.set_mode((window_x, window_y))

    pygame.display.set_caption("Blackjack Game Over")
    game_window.fill(GREEN)

    font = pygame.font.SysFont(None, 50)

    # text setting for chips
    font_obj0 = pygame.font.Font('freesansbold.ttf', 48)
    text_surface_obj0 = font_obj0.render("Chips: " + str(chips - bet), True, BLACK, GREEN)
    text_rect_obj0 = text_surface_obj0.get_rect()
    text_rect_obj0.center = (400, 50)
    game_window.blit(text_surface_obj0, text_rect_obj0)

    # text setting for bet
    font_obj1 = pygame.font.Font('freesansbold.ttf', 48)
    text_surface_obj1 = font_obj1.render("Bet: " + str(bet), True, BLACK, GREEN)
    text_rect_obj1 = text_surface_obj1.get_rect()
    text_rect_obj1.center = (800, 50)
    game_window.blit(text_surface_obj1, text_rect_obj1)

    pcardx, pcardy = (600, 100)
    # Load the card images into the game.
    for card in player.cards:
        pic = pygame.image.load('images/' + str(card) + '.png')
        game_window.blit(pic, (pcardx, pcardy))
        pcardx += 75

    dcardx, dcardy = (100, 100)
    dcard1 = pygame.image.load('images/' + str(dealer.cards[0]) + '.png')
    dcard2 = pygame.image.load('images/' + str(dealer.cards[1]) + '.png')
    dcard_back = pygame.image.load('images/back.png')

    # draw dealer cards
    game_window.blit(dcard1, (dcardx, dcardy))
    game_window.blit(dcard_back, (dcardx + 75, dcardy))

    pygame.display.update()

    clock.tick()

    blackjack = False
    double_prize = False
    dealer_bust = False
    player_bust = False

    # for testing blackjack

    # check if player has blackjack
    if player.value == 21:
        # blackjack text
        add_text('Blackjack!!! You WIN!!', font, game_window, 600, 460, BLACK)
        add_text('Press space to continue', font, game_window, 600, 500, BLACK)
        pygame.display.update()
        blackjack = True
        double_prize = True

    # dealer has natual 21 and player doesnt
    if dealer.value == 21 and player.value != 21:
        add_text('Dealer just got Blackjack. You lose.', font, game_window, 100, 460, BLACK)
        add_text('Press space to continue', font, game_window, 100, 500, BLACK)
        game_window.blit(dcard2, (dcardx + 75, dcardy))
        pygame.display.update()
        blackjack = True




    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

    stand = False
    hand_down = False
    player_wins = False
    dealer_wins = False
    push = False

def game_over():
    window_x = 1200
    window_y = 600
    game_window = pygame.display.set_mode((window_x, window_y))

    pygame.display.set_caption("Blackjack Game Over")
    game_window.fill(GREEN)

    pygame.display.update()
    clock.tick()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

if __name__ == '__main__':
    play()