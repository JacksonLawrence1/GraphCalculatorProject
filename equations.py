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


class Polynomial:
    """
    creates points for a polynomial from linear to quartics
    e.g. x^2, x^3...
    """
    def __init__(self, axis):
        self.points = []  # Each coordinate that the graph goes through
        x_axis = axis.return_x_axis()
        y_axis = axis.return_y_axis()
        # creating instance of x and y axis

        polynomial_degree = self.polynomial_degree()
        polynomial_numbers = [0, 0, 0, 0, 0]
        if polynomial_degree == 4:
            polynomial_numbers[4] = float(input("Enter value for []x^4 >>> "))
        if polynomial_degree >= 3:
            polynomial_numbers[3] = float(input("Enter value for []x^3 >>> "))
        if polynomial_degree >= 2:
            polynomial_numbers[2] = float(input("Enter value for []x^2 >>> "))
        polynomial_numbers[1] = float(input("Enter value for []x >>> "))
        polynomial_numbers[0] = float(input("Enter final value >>> "))
        while x_axis[0] < x_axis[1]:
            y_coordinate = (polynomial_numbers[4] * (x_axis[0]**4))\
                                + (polynomial_numbers[3]*(x_axis[0]**3))\
                                + (polynomial_numbers[2]*(x_axis[0]**2))\
                                + (polynomial_numbers[1] * x_axis[0])\
                                + polynomial_numbers[0]
            if y_axis[0] <= y_coordinate <= y_axis[1]:
                # substitutes numbers into polynomial graph to receive points in valid axis range
                self.points.append([x_axis[0], y_coordinate])
            x_axis[0] += incrementation  # incrementation of x values for each point

    def polynomial_degree(self):
        """
        selection of which graph they want to visualize
        e.g. if degree is 2 then graph will be set to a quadratic
        """
        degree = float(input("Degree of polynomial (1-4) >>> "))
        while degree < 1 or degree > 4 :  # validation loop so user must select 1, 2, 3 or 4
            degree = float(input("Please enter an appropriate value (1-4) >>> "))
        return degree

    def return_points(self):
        return self.points

class Circle:
    def __init__(self, axis):
        """
        creates list of points for circle equation
        """
        self.points = []
        x_axis = axis.return_x_axis()
        y_axis = axis.return_y_axis()
        circle_centre = [0, 0]
        circle_centre[0] = float(input("Enter the x coordinate for centre of circle >>> "))
        circle_centre[1] = float(input("Enter the y coordinate for the centre of circle >>> "))
        circle_radius = float(input("Enter the radius of the circle >>> "))

        start_point = circle_centre[0] - circle_radius
        end_point = circle_centre[0] + circle_radius
        start_point_1 = start_point

        while start_point_1 < end_point:
            circle_b = -(2 * circle_centre[1])
            circle_c = (circle_centre[1] ** 2) + ((start_point_1-circle_centre[0])**2) - (circle_radius ** 2)
            y_coordinate = (-circle_b + math.sqrt((circle_b**2) - (4*circle_c)))/2
            if y_axis[0] <= y_coordinate <= y_axis[1]:
                self.points.append([start_point_1, y_coordinate])
                start_point_1 += incrementation
        while start_point_1 > start_point:
            circle_b = -(2 * circle_centre[1])
            circle_c = (circle_centre[1] ** 2) + ((start_point_1 - circle_centre[0])**2) - (circle_radius ** 2)
            if ((circle_b**2) - (4*circle_c)) > 0:
                y_coordinate = (-circle_b - math.sqrt((circle_b**2) - (4*circle_c)))/2
            if y_axis[0] <= y_coordinate <= y_axis[1]:
                self.points.append([start_point_1, y_coordinate])
            start_point_1 -= incrementation
        self.points.append([start_point, circle_centre[1]])

    def return_points(self):
        return self.points

class Trigonometric:
    """
    function to create trigonometric functions
    e.g. (sin, cos tan graphs)
    """
    def __init__(self, axis):
        """
        creates the list of points for trigonometric functions
        """
        self.points = []
        x_axis = axis.return_x_axis()
        y_axis = axis.return_y_axis()

        trigonometric_function_input = self.trigonometric_function_input()

        while x_axis[0] < x_axis[1]:
            """
            changes what the graph will plot depending on chosen trigonometric function
            """
            if trigonometric_function_input == "SIN":
                y_coordinate = math.sin(x_axis[0])
            elif trigonometric_function_input == "COS":
                y_coordinate = math.cos(x_axis[0])
            elif trigonometric_function_input == "TAN":
                y_coordinate = math.tan(x_axis[0])

            if y_axis[0] <= y_coordinate <= y_axis[1]:
                self.points.append([x_axis[0], y_coordinate])
            x_axis[0] += incrementation

    def trigonometric_function_input(self):
        """
        selection of which type of trigonometric function they
        want to select (e.g. sin, cos, tan)
        """
        trigonometric_function = input("Enter chosen Trigonometric function >>> ").upper()
        while trigonometric_function not in ["SIN", "COS", "TAN"]:
            """
            validation loop, making sure they pick a valid trigonometric function
            """
            trigonometric_function = input("Please enter appropriate function (sin, cos or tan) >>> ").upper()
        return trigonometric_function

    def return_points(self):
        return self.points

class Logarithm:
    def __init__(self, axis):
        self.points = []
        x_axis = axis.return_x_axis()
        y_axis = axis.return_y_axis()

        log_input = self.log_inputs()

        while x_axis[0] < x_axis[1]:
            """
            changes what the graph will plot depending on chosen trigonometric function
            """
            if log_input == "LOG":
                y_coordinate = math.sin(x_axis[0])
            elif log_input == "LN":
                y_coordinate = math.lo(x_axis[0])
            elif log_input == "E":
                y_coordinate = math.tan(x_axis[0])

            if y_axis[0] <= y_coordinate <= y_axis[1]:
                self.points.append([x_axis[0], y_coordinate])
            x_axis[0] += incrementation

    def log_inputs(self):
        """
        what type of log graph they want to plot
        """
        log_input = input("Log, ln or e graph? >>> ").upper()
        while log_input not in ["LOG", "LN", "E"]:
            log_input = input("Please enter an appropriate function (Log, ln or e) >>> ").upper()
        return log_input

    def return_points(self):
        return self.points

