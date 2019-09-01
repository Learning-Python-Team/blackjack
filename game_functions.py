import random
import pygame
import pysnooper

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


def dealer_action(cards, deck):
    """dealer keeps drawing cards until total value is over 16

    :param cards:
    :return: dealer hand
    """
    while cards_value(cards) < 16:
        cards = draw(cards, deck)
    return cards

def draw(cards, deck):
    """ draws a single card and adds it to hand

    :param cards:
    :return: cards + one card
    """
    cards += (deck.pop(),)
    return cards

def card(x,y, card, game_window):
    """create card blit"""
    game_window.blit(card, (x, y))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (66, 245, 123)
RED = (255, 0, 0)
window_width = 1200
window_height = 600
game_window = pygame.display.set_mode((window_width, window_height))

def button(msg,x,y,w,h,ic,ac):
    """draw button function
    :param msg:  msg: What do you want the button to say on it.
    :param x: The x location of the top left coordinate of the button box.
    :param y: The y location of the top left coordinate of the button box.
    :param w: Button width.
    :param h: Button height.
    :param ic: Inactive color (when a mouse is not hovering).
    :param ac: Active color (when a mouse is hovering).
    :return:
    """
    mouse = pygame.mouse.get_pos()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(game_window, ac, (x, y, w, h))
    else:
        pygame.draw.rect(game_window, ic, (x, y, w, h))

    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    game_window.blit(textSurf, textRect)

def text_objects(text, font):
    textSurface = font.render(text, True, WHITE)
    return textSurface, textSurface.get_rect()