import math


# the amount that the x axis will be incremented by
# smaller value the more accurate the graph will look but may take longer to draw
incrementation = 0.01

class Axis:
    """
    Creates numbers for the x and y axis also allowing a range for which the axis can take
    """
    def __init__(self, axis_x_low, axis_x_high, axis_y_low, axis_y_high):
        self.axis_x_low = axis_x_low
        self.axis_x_high = axis_x_high
        self.axis_y_low = axis_y_low
        self.axis_y_high = axis_y_high
        self.x_axis_range = [int(self.axis_x_low), int(self.axis_x_high)]
        self.y_axis_range = [int(self.axis_y_low), int(self.axis_y_high)]

    def return_x_axis(self):
        return self.x_axis_range

    def return_y_axis(self):
        return self.y_axis_range

    def return_local_x_axis(self):
        return [int(self.axis_x_low), int(self.axis_x_high)]

    def return_local_y_axis(self):
        return [int(self.axis_y_low), int(self.axis_y_high)]


class Polynomial:
    """
    creates points for a polynomial from linear to quartics
    e.g. x^2, x^3...
    """
    def __init__(self, axis, polynomial_numbers=(0, 0, 0, 0, 0)):
        local_x_axis = axis.return_local_x_axis()
        local_y_axis = axis.return_local_y_axis()

        self.points = []  # Each coordinate that the graph goes through
        while local_x_axis[0] < local_x_axis[1]:
            y_coordinate = (polynomial_numbers[4] * (local_x_axis[0]**4))\
                                + (polynomial_numbers[3]*(local_x_axis[0]**3))\
                                + (polynomial_numbers[2]*(local_x_axis[0]**2))\
                                + (polynomial_numbers[1] * local_x_axis[0])\
                                + polynomial_numbers[0]
            if local_y_axis[0] <= y_coordinate <= local_y_axis[1]:
                # substitutes numbers into polynomial graph to receive points in valid axis range
                self.points.append([local_x_axis[0], y_coordinate])
            local_x_axis[0] += incrementation  # incrementation of x values for each point

    def return_points(self):
        return self.points


class Circle:
    def __init__(self, axis, circle_centre, circle_radius):
        # creates list of points for circle equation
        self.points = []  # list of coordinates to be plotted in gui

        local_x_axis = axis.return_local_x_axis()
        local_y_axis = axis.return_local_y_axis()

        start_point = circle_centre[0] - circle_radius  # finds range of x coordinates for circle
        end_point = circle_centre[0] + circle_radius
        start_point_1 = start_point  # placeholder for start point allows connection to start coordinate

        while start_point_1 < end_point:
            """
            rearranged equation of a circle to find y coordinate, this first while loop will 
            create the top half/bottom half of the circle depending on the results on the quadratic
            formula
            """
            circle_b = -(2 * circle_centre[1])
            circle_c = (circle_centre[1] ** 2) + ((start_point_1-circle_centre[0])**2) - (circle_radius ** 2)
            y_coordinate = (-circle_b + math.sqrt((circle_b**2) - (4*circle_c)))/2
            if local_y_axis[0] <= y_coordinate <= local_y_axis[1] and local_x_axis[0] <= start_point_1 <= local_x_axis[1]:
                # ensures the coordinate is in the axis range
                self.points.append([start_point_1, y_coordinate])
            start_point_1 += incrementation
        while start_point_1 > start_point:
            circle_b = -(2 * circle_centre[1])
            circle_c = (circle_centre[1] ** 2) + ((start_point_1 - circle_centre[0])**2) - (circle_radius ** 2)
            if ((circle_b**2) - (4*circle_c)) > 0:
                y_coordinate = (-circle_b - math.sqrt((circle_b**2) - (4*circle_c)))/2
            if local_y_axis[0] <= y_coordinate <= local_y_axis[1] and local_x_axis[0] <= start_point_1 <= local_x_axis[1]:
                self.points.append([start_point_1, y_coordinate])
            start_point_1 -= incrementation
        if local_y_axis[0] <= start_point <= local_y_axis[1] and local_x_axis[0] <= circle_centre[1] <= local_x_axis[1]:
            self.points.append([start_point, circle_centre[1]])  # connects last coordinate to first point

    def return_points(self):
        return self.points


class Trigonometric:
    """
    function to create trigonometric functions
    e.g. (sin, cos tan graphs)
    """
    def __init__(self, axis, trigonometric_function_input, x_coefficient=1, function_coefficient=1):
        """
        creates the list of points for trigonometric functions
        """
        self.points = []

        local_x_axis = axis.return_local_x_axis()
        local_y_axis = axis.return_local_y_axis()

        while local_x_axis[0] <= local_x_axis[1]:
            """
            changes what the graph will plot depending on chosen trigonometric function
            """
            if trigonometric_function_input == "SIN":
                y_coordinate = function_coefficient * (math.sin(x_coefficient * local_x_axis[0]))
            elif trigonometric_function_input == "COS":
                y_coordinate = function_coefficient * (math.cos(x_coefficient * local_x_axis[0]))
            elif trigonometric_function_input == "TAN":
                y_coordinate = function_coefficient * (math.tan(x_coefficient * local_x_axis[0]))

            if local_y_axis[0] <= y_coordinate <= local_y_axis[1]:
                # starts adding coordinates to list of points within given axis range
                self.points.append([local_x_axis[0], y_coordinate])
            local_x_axis[0] += incrementation

    def return_points(self):
        return self.points


class Logarithm:
    def __init__(self, axis, log_input, log_base=0):
        self.points = []

        local_x_axis = axis.return_local_x_axis()
        local_y_axis = axis.return_local_y_axis()

        next_y_axis = True
        while local_x_axis[0] < local_x_axis[1]:
            """
            changes what the graph will plot depending on chosen trigonometric function
            """
            if local_x_axis[0] > 0:
                next_y_axis = True
                if log_input == "LOG":
                    y_coordinate = math.log(local_x_axis[0], log_base)
                elif log_input == "LN":
                    y_coordinate = math.log(local_x_axis[0], 2.71828182845)  # accurate value for e
                elif log_input == "E":
                    y_coordinate = 2.71828182845 ** local_x_axis[0]
            elif log_input == "E":
                y_coordinate = 2.71828182845 ** local_x_axis[0]
            else:
                next_y_axis = False

            if next_y_axis:
                if local_y_axis[0] <= y_coordinate <= local_y_axis[1]:
                    self.points.append([local_x_axis[0], y_coordinate])
            local_x_axis[0] += incrementation

    def return_points(self):
        return self.points


