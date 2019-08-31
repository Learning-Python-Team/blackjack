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

y = (window_height * .1)
pc1_x = (window_width * .500)
pc2_x = (window_width * .550)
pc3_x = (window_width * .600)
pc4_x = (window_width * .650)
pc5_x = (window_width * .700)
pc6_x = (window_width * .750)

dealer1_x = (window_width * .050)
dealer2_x = (window_width * .100)
dealer3_x = (window_width * .150)
dealer4_x = (window_width * .200)
dealer5_x = (window_width * .250)
dealer6_x = (window_width * .300)

# Create a shoe of 6 decks of cards 'RankSuit'
deck = game_functions.create_deck()

# pop two cards for player and dealer
player_card1 = deck.pop()
player_card2 = deck.pop()
player_card3 = deck.pop()
player_card4 = deck.pop()
player_card5 = deck.pop()
player_card6 = deck.pop()

dealer_card1 = deck.pop()
dealer_card2 = deck.pop()
dealer_card3 = deck.pop()
dealer_card4 = deck.pop()
dealer_card5 = deck.pop()
dealer_card6 = deck.pop()

while game_running:

    # gets 6 cards for player and dealer
    player_card1_image = pygame.image.load(cards.card_conversion(player_card1))
    player_card2_image = pygame.image.load(cards.card_conversion(player_card2))
    player_card3_image = pygame.image.load(cards.card_conversion(player_card3))
    player_card4_image = pygame.image.load(cards.card_conversion(player_card4))
    player_card5_image = pygame.image.load(cards.card_conversion(player_card5))
    player_card6_image = pygame.image.load(cards.card_conversion(player_card6))

    dealer_card1_image = pygame.image.load(cards.card_conversion(dealer_card1))
    dealer_card2_image = pygame.image.load(cards.card_conversion(dealer_card2))
    dealer_card3_image = pygame.image.load(cards.card_conversion(dealer_card3))
    dealer_card4_image = pygame.image.load(cards.card_conversion(dealer_card4))
    dealer_card5_image = pygame.image.load(cards.card_conversion(dealer_card5))
    dealer_card6_image = pygame.image.load(cards.card_conversion(dealer_card6))


    # Loop through all active events
    for event in pygame.event.get():
        # Close the program if the user presses the 'X'
        if event.type == pygame.QUIT:
            game_running = False

    # Content here
    game_window.fill((66, 245, 123))
    card(dealer1_x, y, dealer_card1_image)
    card(dealer2_x, y, dealer_card2_image)
    card(dealer3_x, y, dealer_card3_image)
    card(dealer4_x, y, dealer_card4_image)
    card(dealer5_x, y, dealer_card5_image)
    card(dealer6_x, y, dealer_card6_image)

    card(pc1_x, y, player_card1_image)
    card(pc2_x, y, player_card2_image)
    card(pc3_x, y, player_card3_image)
    card(pc4_x, y, player_card4_image)
    card(pc5_x, y, player_card5_image)
    card(pc6_x, y, player_card6_image)
    # Update our display
    pygame.display.update()

# Uninitialize all pygame modules and quit the program
pygame.quit()
sys.exit()

