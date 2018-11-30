import math

# the amount that the x axis will be incremented by
# smaller value the more accurate the graph will look but may take longer to draw
incrementation = 0.01

class Axis:
    """
    Creates numbers for the x and y axis also allowing a range for which the axis can take
    """
    def __init__(self, axis_x_low, axis_x_high, axis_y_low, axis_y_high):
        self.x_axis_range = [int(axis_x_low), int(axis_x_high)]
        self.y_axis_range = [int(axis_y_low), int(axis_y_high)]

    def return_x_axis(self):
        return self.x_axis_range

    def return_y_axis(self):
        return self.y_axis_range

class Equation:
    def __init__(self, axis):
        self.x_axis = axis.return_x_axis()
        self.y_axis = axis.return_y_axis()
        self.list_of_points = []

    def return_points(self):
        return self.list_of_points


class Polynomial(Equation):
    """
    creates points for a polynomial from linear to quartics
    e.g. x^2, x^3...
    """
    def __init__(self, axis, polynomial_numbers):
        super().__init__(axis)
        self.points = []  # Each coordinate that the graph goes through
        while self.x_axis[0] < self.x_axis[1]:
            y_coordinate = (polynomial_numbers[4] * (self.x_axis[0]**4))\
                                + (polynomial_numbers[3]*(self.x_axis[0]**3))\
                                + (polynomial_numbers[2]*(self.x_axis[0]**2))\
                                + (polynomial_numbers[1] * self.x_axis[0])\
                                + polynomial_numbers[0]
            if self.y_axis[0] <= y_coordinate <= self.y_axis[1]:
                # substitutes numbers into polynomial graph to receive points in valid axis range
                self.points.append([self.x_axis[0], y_coordinate])
            self.x_axis[0] += incrementation  # incrementation of x values for each point

    def return_points(self):
        return self.points


class Circle(Equation):
    def __init__(self, axis, circle_centre, circle_radius):
        super().__init__(axis)
        """
        creates list of points for circle equation
        """

        self.points = []

        start_point = circle_centre[0] - circle_radius
        end_point = circle_centre[0] + circle_radius
        start_point_1 = start_point

        while start_point_1 < end_point:
            circle_b = -(2 * circle_centre[1])
            circle_c = (circle_centre[1] ** 2) + ((start_point_1-circle_centre[0])**2) - (circle_radius ** 2)
            y_coordinate = (-circle_b + math.sqrt((circle_b**2) - (4*circle_c)))/2
            if self.y_axis[0] <= y_coordinate <= self.y_axis[1]:
                self.points.append([start_point_1, y_coordinate])
                start_point_1 += incrementation
        while start_point_1 > start_point:
            circle_b = -(2 * circle_centre[1])
            circle_c = (circle_centre[1] ** 2) + ((start_point_1 - circle_centre[0])**2) - (circle_radius ** 2)
            if ((circle_b**2) - (4*circle_c)) > 0:
                y_coordinate = (-circle_b - math.sqrt((circle_b**2) - (4*circle_c)))/2
            if self.y_axis[0] <= y_coordinate <= self.y_axis[1]:
                self.points.append([start_point_1, y_coordinate])
            start_point_1 -= incrementation
        self.points.append([start_point, circle_centre[1]])

    def return_points(self):
        return self.points

class Trigonometric(Equation):
    """
    function to create trigonometric functions
    e.g. (sin, cos tan graphs)
    """
    def __init__(self, axis, trigonometric_function_input):
        super().__init__(axis)
        """
        creates the list of points for trigonometric functions
        """
        self.points = []

        while self.x_axis[0] < self.x_axis[1]:
            """
            changes what the graph will plot depending on chosen trigonometric function
            """
            if trigonometric_function_input == "SIN":
                y_coordinate = math.sin(self.x_axis[0])
            elif trigonometric_function_input == "COS":
                y_coordinate = math.cos(self.x_axis[0])
            elif trigonometric_function_input == "TAN":
                y_coordinate = math.tan(self.x_axis[0])

            if self.y_axis[0] <= y_coordinate <= self.y_axis[1]:
                self.points.append([self.x_axis[0], y_coordinate])
            self.x_axis[0] += incrementation

    def return_points(self):
        return self.points


class Logarithm(Equation):
    def __init__(self, axis, log_input):
        super().__init__(axis)
        self.points = []

        next_y_axis = True
        while self.x_axis[0] < self.x_axis[1]:
            """
            changes what the graph will plot depending on chosen trigonometric function
            """
            if self.x_axis[0] > 0:
                next_y_axis = True
                if log_input[0] == "LOG":
                    y_coordinate = math.log(self.x_axis[0], log_input[1])
                elif log_input[0] == "LN":
                    y_coordinate = math.log(self.x_axis[0], 2.71828182845)  # accurate value for e
                elif log_input[0] == "E":
                    y_coordinate = 2.71828182845 ** self.x_axis[0]
            elif log_input[0] == "E":
                y_coordinate = 2.71828182845 ** self.x_axis[0]
            else:
                next_y_axis = False

            if next_y_axis:
                if self.y_axis[0] <= y_coordinate <= self.y_axis[1]:
                    self.points.append([self.x_axis[0], y_coordinate])
            self.x_axis[0] += incrementation

    def return_points(self):
        return self.points

