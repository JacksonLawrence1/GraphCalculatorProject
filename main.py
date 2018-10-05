import math


class Axis:
    """
    Creates numbers for the x and y axis also allowing a range for which the axis can take
    """
    def __init__(self, axis_x_low, axis_x_high, axis_y_low, axis_y_high):
        self.x_axis_range = [axis_x_low, axis_x_high]
        self.y_axis_range = [axis_y_low, axis_y_high]
        self.x_axis_difference = self.x_axis_range[1] - self.x_axis_range[0]
        self.y_axis_difference = self.y_axis_range[1] - self.y_axis_range[0]


class Polynomial:
    """
    creates points for a polynomial from quadratics to quartics
    e.g. x^2, x^3...
    """
    def __init__(self, axis):
        self.list_of_points = []
        x_axis_low = int(axis.x_axis_range[0])
        x_axis_high = int(axis.x_axis_range[1])
        y_axis_low = int(axis.y_axis_range[0])
        y_axis_high = int(axis.y_axis_range[1])

        polynomial_numbers = [0, 0, 0, 0, 0]
        if self.polynomial_degree() == 4:
            polynomial_numbers[4] = int(input("Enter value for []x^4 >>> "))
        elif self.polynomial_degree() == 3:
            polynomial_numbers[3] = int(input("Enter value for []x^3 >>> "))
        elif self.polynomial_degree() == 2:
            polynomial_numbers[2] = int(input("Enter value for []x^2 >>> "))
        else:
            polynomial_numbers[1] = int(input("Enter value for []x >>> "))
        polynomial_numbers[0] = int(input("Enter final value >>> "))
        while x_axis_low < x_axis_high:
            if y_axis_low <= (polynomial_numbers[0] * (x_axis_low**4)) + (polynomial_numbers[1]*(x_axis_low**3)) + (polynomial_numbers[2]*(x_axis_low**2)) + (polynomial_numbers[3] * x_axis_low) + polynomial_numbers[4] <= y_axis_high:
                # substitutes numbers into quartic graph to receive points in valid axis range
                self.list_of_points.append([x_axis_low, (polynomial_numbers[0] * (x_axis_low**4)) + (polynomial_numbers[1]*(x_axis_low**3)) + (polynomial_numbers[2]*(x_axis_low**2)) + (polynomial_numbers[3] * x_axis_low) + polynomial_numbers[4]])
            x_axis_low += 1  # incrementation of x values for each point

        print(self.list_of_points)

    def polynomial_degree(self):
        """
        selection of which graph they want to visualize
        e.g. if degree is 2 then graph will be set to a quadratic
        """
        degree = int(input("Degree of polynomial (2-4) >>> "))
        while 2 < degree < 5: # validation loop so user must select 2, 3 or 4
            degree = int(input("Please enter an appropriate value (2-4): "))
        return degree


graph_axis = Axis(-10, 10, -10, 10)
Polynomial(graph_axis)

class Trigonometric:
    pass


class Circle:
    pass


class Logarithm:
    pass
