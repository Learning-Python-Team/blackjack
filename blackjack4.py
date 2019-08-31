"""
 Pygame base template for opening a window

"""

import pygame
import cards
import game_functions as gf

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (66, 245, 123)
RED = (255, 0, 0)

pygame.init()

# Set the width and height of the screen [width, height]
window_width = 1200
window_height = 600
gameDisplay = pygame.display.set_mode((window_width, window_height))

pygame.display.set_caption("Blackjack")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Create a shoe of 6 decks of cards 'RankSuit'
deck = gf.create_deck()

# create card screen locations
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

# player draws two cards
player_card1 = deck.pop()
player_card2 = deck.pop()

# dealer draws two cards
dealer_card1 = deck.pop()
dealer_card2 = deck.pop()
dealer_back = "back"

# text setting
font_obj = pygame.font.Font('freesansbold.ttf', 32)
text_surface_obj = font_obj.render("Dealer's Hand", True, BLACK, GREEN)
text_rect_obj = text_surface_obj.get_rect()
text_rect_obj.center = (window_width * .20, window_height * .050)

# text setting
font_obj1 = pygame.font.Font('freesansbold.ttf', 32)
text_surface_obj1 = font_obj1.render("Player's Hand", True, BLACK, GREEN)
text_rect_obj1 = text_surface_obj1.get_rect()
text_rect_obj1.center = (window_width * .70, window_height * .050)


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    gameDisplay.fill(GREEN)
    # draw the text onto the surface
    gameDisplay.blit(text_surface_obj, text_rect_obj)
    gameDisplay.blit(text_surface_obj1, text_rect_obj1)
    # create card images
    player_card1_image = pygame.image.load(cards.card_conversion(player_card1))
    player_card2_image = pygame.image.load(cards.card_conversion(player_card2))

    # display cards
    gf.card(pc1_x, y, player_card1_image, gameDisplay)
    gf.card(pc2_x, y, player_card2_image, gameDisplay)

    # create card images
    dealer_back_image = pygame.image.load(cards.card_conversion(dealer_back))
    dealer_card1_image = pygame.image.load(cards.card_conversion(dealer_card1))
    dealer_card2_image = pygame.image.load(cards.card_conversion(dealer_card2))

    # display one card and show one back
    gf.card(dealer1_x, y, dealer_card1_image, gameDisplay)
    gf.card(dealer2_x, y, dealer_back_image, gameDisplay)

    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    # screen.fill(GREEN)

    # --- Drawing code should go here

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
