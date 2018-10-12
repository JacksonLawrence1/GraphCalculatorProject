# creates the screen with axis

import pygame

# Initialises the pygame module
pygame.init()

height = 720
width = 1280
screen_size = (width, height)  # Sets screen size
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Graph Calculator")  # Title of game at the top

WHITE = (255, 255, 255)

repeat = True

while repeat:  # Main event loop

    for event in pygame.event.get():
        """
        If player presses the x in the top right, the game will close.
        """
        if event.type == pygame.QUIT:
            repeat = False

    screen.fill(WHITE)

    pygame.display.flip()  # Updates window's display

pygame.quit()