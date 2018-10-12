import math


class Axis:
    """
    Creates numbers for the x and y axis also allowing a range for which the axis can take
    """
    def __init__(self, axis_x_low, axis_x_high, axis_y_low, axis_y_high):
        self.x_axis_range = [int(axis_x_low), int(axis_x_high)]
        self.y_axis_range = [int(axis_y_low), int(axis_y_high)]
        self.x_axis_difference = self.x_axis_range[1] - self.x_axis_range[0]
        self.y_axis_difference = self.y_axis_range[1] - self.y_axis_range[0]

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
        self.list_of_points = []  # Each coordinate that the graph goes through
        x_axis = graph_axis.return_x_axis()
        y_axis = graph_axis.return_y_axis()
        # creating instance of x and y axis

        polynomial_degree = self.polynomial_degree()
        polynomial_numbers = [0, 0, 0, 0, 0]
        if polynomial_degree == 4:
            polynomial_numbers[4] = int(input("Enter value for []x^4 >>> "))
        elif polynomial_degree == 3:
            polynomial_numbers[3] = int(input("Enter value for []x^3 >>> "))
        elif polynomial_degree == 2:
            polynomial_numbers[2] = int(input("Enter value for []x^2 >>> "))
        polynomial_numbers[1] = int(input("Enter value for []x >>> "))
        polynomial_numbers[0] = int(input("Enter final value >>> "))
        while x_axis[0] < x_axis[1]:
            if y_axis[0] <= (polynomial_numbers[4] * (x_axis[0]**4))\
                    + (polynomial_numbers[3]*(x_axis[0]**3))\
                    + (polynomial_numbers[2]*(x_axis[0]**2))\
                    + (polynomial_numbers[1] * x_axis[0])\
                    + polynomial_numbers[0] <= y_axis[1]:
                # substitutes numbers into polynomial graph to receive points in valid axis range
                self.list_of_points.append([x_axis[0], (polynomial_numbers[4] * (x_axis[0]**4))
                                            + (polynomial_numbers[3]*(x_axis[0]**3))
                                            + (polynomial_numbers[2]*(x_axis[0]**2))
                                            + (polynomial_numbers[1] * x_axis[0])
                                            + polynomial_numbers[0]])
            x_axis[0] += 1  # incrementation of x values for each point

        print(self.list_of_points)

    def polynomial_degree(self):
        """
        selection of which graph they want to visualize
        e.g. if degree is 2 then graph will be set to a quadratic
        """
        degree = int(input("Degree of polynomial (1-4) >>> "))
        while degree < 1 or degree > 4 : # validation loop so user must select 1, 2, 3 or 4
            degree = int(input("Please enter an appropriate value (1-4) >>> "))
        return degree


graph_axis = Axis(-10, 10, -10, 10)
Polynomial(graph_axis)

class Trigonometric:
    pass


class Circle:
    pass


class Logarithm:
    pass