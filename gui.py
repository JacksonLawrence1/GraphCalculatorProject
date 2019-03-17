
# creates the screen with axis
import equations
import pygame
from pygame.locals import *
from importlib import reload

modules_imported = ["equations"]

# Initialises the pygame module
pygame.init()

height = 720
width = 720
screen_size = (width, height)  # Sets screen size
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Graph Calculator")  # Title of game at the top

# colour constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GRAY = (141, 148, 160)

font = pygame.font.SysFont('Comic Sans MS', 15, True, False)  # font used for normal text
title_font = pygame.font.SysFont('Comic Sans MS', 48, True, False)

def text_objects(text, font):
    # renders a text surface
    textSurface = font.render(text, True, WHITE)
    return textSurface, textSurface.get_rect()


def button(text, x, y, width, height, inactive_colour, active_colour):
    # function to draw a button to screen
    mouse = pygame.mouse.get_pos()

    if x+width > mouse[0] > x and y+height > mouse[1] > y:
        pygame.draw.rect(screen, active_colour, (x, y, width, height))
    else:
        pygame.draw.rect(screen, inactive_colour, (x, y, width, height))

    smallText = pygame.font.SysFont('Comic Sans MS', 20)
    textSurf, textRect = text_objects(text, smallText)
    textRect.center = ((x + (width / 2)), (y + (height / 2)))
    screen.blit(textSurf, textRect)


# standardizing coordinates from array
def standardize_coordinates(coordinates):
    for item in coordinates:
        item[0] = (item[0] + (x_axis_difference / 2)) * x_factor
        item[1] = abs(item[1] - (y_axis_difference / 2)) * y_factor
    return coordinates


equation_coordinates_1 = ([0,0], [0,0])
equation_coordinates_2 = ([0,0], [0,0])
equation_coordinates_3 = ([0,0], [0,0])

equation_coordinates_1_bool = False
equation_coordinates_2_bool = False
equation_coordinates_3_bool = False

standardize_1_bool = True
standardize_2_bool = True
standardize_3_bool = True

equation_axis = equations.Axis(-10, 10, -10, 10)

repeat = True
graph_menu = False
start_menu = True

while repeat:  # Main event loop
    mouse = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()

    for event in pygame.event.get():
        """
        If player presses 
        repeat = True
        the x in the top right, the game will close.
        """
        if event.type == pygame.QUIT:
            repeat = False

        screen.fill(WHITE)  # fill screen with white background

        if start_menu:
            """
            main menu with buttons
            """
            title = title_font.render("Graph Calculator", True, BLACK)
            screen.blit(title, (160, 150))

            start_button = button("Start", 300, 300, 100, 40, (47, 178, 14), (66, 244, 110))
            quit_button = button("Quit", 300, 400, 100, 40, RED, (244, 92, 66))

            if 300 < mouse[0] < 400 and 300 < mouse[1] < 340:
                    if event.type == MOUSEBUTTONDOWN:
                        start_menu = False
                        graph_menu = True
            if 300 < mouse[0] < 400 and 400 < mouse[1] < 440:
                    if event.type == MOUSEBUTTONDOWN:
                        repeat = False

        elif graph_menu:

            x_axis_difference = equation_axis.return_x_axis()[1] - equation_axis.return_x_axis()[0]
            y_axis_difference = equation_axis.return_y_axis()[1] - equation_axis.return_y_axis()[0]
            x_factor = width / x_axis_difference
            y_factor = height / y_axis_difference

            for i in range(0, width, int(width * 0.05)):
                """
                draws graph lines
                """
                vertical_line = pygame.Surface((1, width), pygame.SRCALPHA)
                vertical_line.fill((141, 148, 160, 75))  # change the 100 depending on what transparency it is.
                screen.blit(vertical_line, (i, 0))
                horizontal_line = pygame.Surface((width, 1), pygame.SRCALPHA)
                horizontal_line.fill((141, 148, 160, 75))  # change the 100 depending on what transparency it is
                screen.blit(horizontal_line, (0, i))

            pygame.draw.line(screen, BLACK, (width / 2, 0), (width / 2, height), 5)  # creates y axis line
            pygame.draw.line(screen, BLACK, (0, height / 2), (width, height / 2), 5)  # creates x axis line

            axis_counter_height = equation_axis.return_y_axis()[1]
            for i in range(0, height, int(height * 0.05)):
                """
                draws numbers along y axis
                """
                axis_number = font.render("{:.0f}".format(axis_counter_height), True, BLACK)  # ensures no decimals
                if axis_counter_height == 0:
                    screen.blit(axis_number, ((width/2) - 4, (height/2) - 10))
                elif axis_counter_height > 0:
                    screen.blit(axis_number, ((width/2)-18, i-10))
                else:
                    screen.blit(axis_number, ((width/2)-28, i-10))
                axis_counter_height -= y_axis_difference * 0.05

            axis_counter_width = equation_axis.return_x_axis()[0]
            for i in range(0, width, int(width * 0.05)):
                """
                draws numbers along x axis
                """
                axis_number = font.render("{:.0f}".format(axis_counter_width), True, BLACK)  # ensures no decimals
                if axis_counter_width > 0:
                    screen.blit(axis_number, (i-5, height/2))
                elif axis_counter_width < 0:
                    screen.blit(axis_number, (i-12, height/2))
                axis_counter_width += x_axis_difference * 0.05

            # Renders buttons to the screen - does not actually do any function
            main_menu_button =  button("Menu", 50, 50, 80 , 40, RED, (244, 92, 66))
            new_graph_button_1 = button("New Graph 1", 550, 50, 120, 40, RED, (244, 92, 66))
            new_graph_button_2 = button("New Graph 2", 550, 100, 120, 40, (50, 78, 219), (94, 116, 229))
            new_graph_button_3 = button("New Graph 3", 550, 150, 120, 40, (26, 165, 79), (51, 214, 113))

            if 550 < mouse[0] < 670 and 50 < mouse[1] < 90:
                # creates graph for 1st button
                if event.type == MOUSEBUTTONDOWN:
                    equation_coordinates_1_bool = True
                    if "equation_inputs" not in modules_imported:
                        modules_imported.append("equation_inputs")
                        import equation_inputs
                    else:
                        reload(equation_inputs)
                    equation_coordinates_1 = equation_inputs.equation_coordinates
                    standardize_coordinates(equation_coordinates_1)

            if 550 < mouse[0] < 670 and 100 < mouse[1] < 140:
                # creates graph for 2nd button
                if event.type == MOUSEBUTTONDOWN:
                    equation_coordinates_2_bool = True
                    if "equation_inputs" not in modules_imported:
                        modules_imported.append("equation_inputs")
                        import equation_inputs
                    else:
                        reload(equation_inputs)
                    equation_coordinates_2 = equation_inputs.equation_coordinates
                    standardize_coordinates(equation_coordinates_2)

            if 550 < mouse[0] < 670 and 150 < mouse[1] < 190:
                # creates graph for 3rd button
                if event.type == MOUSEBUTTONDOWN:
                    equation_coordinates_3_bool = True
                    if "equation_inputs" not in modules_imported:
                        modules_imported.append("equation_inputs")
                        import equation_inputs
                    else:
                        reload(equation_inputs)
                    equation_coordinates_3 = equation_inputs.equation_coordinates
                    standardize_coordinates(equation_coordinates_3)

            if equation_coordinates_1_bool:
                # creates reset button once graph is drawn
                reset_graph_button_2 = button("x", 680, 60, 20, 20, RED, (244, 92, 66))
            if 680 < mouse[0] < 700 and 60 < mouse[1] < 80:
                # if user clicks reset button graph is deleted
                    if event.type == MOUSEBUTTONDOWN:
                        equation_coordinates_1 = [(0,0), (0,0)]
                        equation_coordinates_1_bool = False

            if equation_coordinates_2_bool:
                reset_graph_button_2 = button("x", 680, 110, 20, 20, (50, 78, 219), (94, 116, 229))
            if 680 < mouse[0] < 700 and 110 < mouse[1] < 130:
                    if event.type == MOUSEBUTTONDOWN:
                        equation_coordinates_2 = [(0,0), (0,0)]
                        equation_coordinates_2_bool = False

            if equation_coordinates_3_bool:
                reset_graph_button_2 = button("x", 680, 160, 20, 20, (26, 165, 79), (51, 214, 113))
            if 680 < mouse[0] < 700 and 160 < mouse[1] < 180:
                    if event.type == MOUSEBUTTONDOWN:
                        equation_coordinates_3 = [(0,0), (0,0)]
                        equation_coordinates_3_bool = False

            if 50 < mouse[0] < 130 and 50 < mouse[1] < 90:
                    if event.type == MOUSEBUTTONDOWN:
                        graph_menu = False
                        start_menu = True

            axis_range_button = button("Change Axis", 550, 650, 120, 40, RED, (244, 92, 66))

            if 550 < mouse[0] < 670 and 650 < mouse[1] < 690:
                # creates graph for 3rd button
                if event.type == MOUSEBUTTONDOWN:
                    if "equation_inputs" not in modules_imported:
                        modules_imported.append("equation_inputs")
                        import equation_inputs
                    else:
                        reload(equation_inputs)
                    equation_inputs.axis_bool = False

                    if "axis_input" not in modules_imported:
                        modules_imported.append("axis_input")
                        import axis_input
                    else:
                        reload(axis_input)
                    equation_axis = axis_input.axis

            pygame.draw.lines(screen, RED, False, equation_coordinates_1, 2)  # draws equation of line
            pygame.draw.lines(screen, (50, 78, 219), False, equation_coordinates_2, 2)  # draws equation of line
            pygame.draw.lines(screen, (26, 165, 79), False, equation_coordinates_3, 2)  # draws equation of line

    pygame.display.flip()  # Updates window's display

pygame.quit()
