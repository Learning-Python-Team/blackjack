import pygame
import sys
import cards
import game_functions

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (66, 245, 123)
RED = (255, 0, 0)

window_width = 1200
window_height = 700

pygame.init()
clock = pygame.time.Clock()
init_result = pygame.init()
print(init_result)

# Create a game window
game_window = pygame.display.set_mode((window_width, window_height))

# Set title
pygame.display.set_caption("Blackjack")

game_running = True


def card(x, y, crd):
    game_window.blit(crd, (x, y))


def text_objects(text, font):
    text_surface = font.render(text, True, WHITE)
    return text_surface, text_surface.get_rect()

def button(msg,x,y,w,h,ic,ac, action=None):
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
    click = pygame.mouse.get_pressed()
    print(click)

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(game_window, ac, (x, y, w, h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(game_window, ic, (x, y, w, h))

    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    game_window.blit(textSurf, textRect)

def draw_card():
    count = 2
    card(pc1_x, y, player_card1_image)
    card(pc2_x, y, player_card2_image)
    card(pc3_x, y, player_card3_image)

def stick():
    sys.exit()

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

    game_window.blit(text_surface_obj, text_rect_obj)
    game_window.blit(text_surface_obj1, text_rect_obj1)

    card(dealer1_x, y, dealer_card1_image)
    card(dealer2_x, y, dealer_card2_image)
    card(dealer3_x, y, dealer_card3_image)
    card(dealer4_x, y, dealer_card4_image)
    card(dealer5_x, y, dealer_card5_image)
    card(dealer6_x, y, dealer_card6_image)

    card(pc1_x, y, player_card1_image)
    card(pc2_x, y, player_card2_image)
    #card(pc3_x, y, player_card3_image)
    #card(pc4_x, y, player_card4_image)

    #card(pc5_x, y, player_card5_image)
    #card(pc6_x, y, player_card6_image)
    """
    mouse = pygame.mouse.get_pos()
    # draw hit button
    if (window_width * .500) + 200 > mouse[0] > 600 and 450 + 50 > mouse[1] > 450:
        pygame.draw.rect(game_window, BLACK, ((window_width * .500), 450, 200, 50))
    else:
        pygame.draw.rect(game_window, RED, ((window_width * .500), 450, 200, 50))
    # draw stand button
    if (window_width * .750) + 200 > mouse[0] > (window_width * .750) and 450 + 50 > mouse[1] > 450:
        pygame.draw.rect(game_window, BLACK, ((window_width * .750), 450, 200, 50))
    else:
        pygame.draw.rect(game_window, RED, ((window_width * .750), 450, 200, 50))

    #button(msg, x, y, w, h, ic, ac)
    

    # hit button text
    
    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects("HIT!", smallText)
    textRect.center = (((window_width * .500) + 100), (450 + (50 / 2)))
    game_window.blit(textSurf, textRect)
    
    # stick button text
    textSurf, textRect = text_objects("STICK!", smallText)
    textRect.center = (((window_width * .750) + 100), (450 + (50 / 2)))
    game_window.blit(textSurf, textRect)
    """
    button("Hit!", ((window_width * .500)), (450 + (50 / 2)), 200, 50, BLACK, RED, draw_card)
    button("Stick!", ((window_width * .750)), (450 + (50 / 2)), 200, 50, BLACK, RED, stick)

    # pygame.draw.rect(game_window, RED, ((window_width * .500), 450, 100, 50))
    # Update our display
    pygame.display.update()
    # refresh rate
    clock.tick(60)

# Uninitialize all pygame modules and quit the program
pygame.quit()
sys.exit()
