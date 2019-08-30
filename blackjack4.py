"""
 Pygame base template for opening a window

"""

import pygame
import cards

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

# Set the width and height of the screen [width, height]
#size = (1200, 600)
#screen = pygame.display.set_mode(size)
display_width = 1000
display_height = 800
gameDisplay = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption("Blackjack")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

card_image = pygame.image.load(cards.card_conversion("2H"))
card_image2 = pygame.image.load(cards.card_conversion('AC'))
def card(x,y, card):
    gameDisplay.blit(card, (x, y))

x = (display_width * 0.45)
y = (display_height * .1)
z = (display_width * .55)

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    gameDisplay.fill(GREEN)
    card(x, y, card_image)
    card(z, y, card_image2)

    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    #screen.fill(GREEN)

    # --- Drawing code should go here

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()