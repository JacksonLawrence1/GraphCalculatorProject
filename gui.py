# creates the screen with axis
import equations
import pygame
from itertools import cycle

# Initialises the pygame module
pygame.init()

x_axis = (-10, 10)
y_axis = (-10, 10)

graph_axis = equations.Axis(x_axis[0], x_axis[1], y_axis[0], y_axis[1])

height = 720
width = 1280
screen_size = (width, height)  # Sets screen size
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Graph Calculator")  # Title of game at the top

# colour constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

x_axis_difference = x_axis[1] - x_axis[0]
y_axis_difference = y_axis[1] - y_axis[0]

# multiplication factor for coordinate and screen size
x_factor = width / x_axis_difference
y_factor = height / y_axis_difference

equation_coordinates = equations.Polynomial(graph_axis).points
for item in equation_coordinates:
    item[0] = (item[0] + (x_axis_difference / 2)) * x_factor
    item[1] = abs(item[1] - (y_axis_difference / 2)) * y_factor

repeat = True

while repeat:  # Main event loop

    for event in pygame.event.get():
        """
        If player presses the x in the top right, the game will close.
        """
        if event.type == pygame.QUIT:
            repeat = False

    screen.fill(WHITE)

    pygame.draw.line(screen, BLACK, (0, height / 2), (width, height / 2), 5)
    pygame.draw.line(screen, BLACK, (width / 2, 0), (width / 2, height), 5)

    pygame.draw.lines(screen, RED, False, equation_coordinates, 3)

    pygame.display.flip()  # Updates window's display

pygame.quit()