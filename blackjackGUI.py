import pygame
import sys
import cards
import game_functions




window_width = 1200
window_height = 700

pygame.init()

init_result = pygame.init()
print(init_result)

# Create a game window
game_window = pygame.display.set_mode((window_width, window_height))

# Set title
pygame.display.set_caption("Blackjack")

game_running = True

def card(x,y, card):
    game_window.blit(card, (x, y))

x = (window_width * 0.5)
y = (window_height * .1)
z = (window_width * .6)

dealer1_x = (window_width * .1)
dealer2_x = (window_width * .2)

# Create a shoe of 6 decks of cards 'RankSuit'
deck = game_functions.create_deck()

# pop two cards for player and dealer
player_card1, player_card2 = deck.pop(), deck.pop()
dealer_card1, dealer_card2 = deck.pop(), deck.pop()

while game_running:


    # gets first two cards for player and dealer


    player_card1_image = pygame.image.load(cards.card_conversion(player_card1))
    player_card2_image = pygame.image.load(cards.card_conversion(player_card2))

    dealer_card1_image = pygame.image.load(cards.card_conversion(dealer_card1))
    dealer_card2_image = pygame.image.load(cards.card_conversion(dealer_card2))

    # Loop through all active events
    for event in pygame.event.get():
        # Close the program if the user presses the 'X'
        if event.type == pygame.QUIT:
            game_running = False

    # Content here
    game_window.fill((66, 245, 123))
    card(dealer1_x, y, dealer_card1_image)
    card(dealer2_x, y, dealer_card2_image)

    card(x, y, player_card1_image)
    card(z, y, player_card2_image)
    # Update our display
    pygame.display.update()

# Uninitialize all pygame modules and quit the program
pygame.quit()
sys.exit()

