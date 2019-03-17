import equations
from importlib import reload

axis_bool = True


def polynomial_input(degree):
    """
    selection of which graph they want to visualize
    e.g. if degree is 2 then graph will be set to a quadratic
    """
    while degree < 1 or degree > 4:  # validation loop so user must select 1, 2, 3 or 4
        degree = input("Please enter an appropriate value (1-4) >>> ")
    polynomial_numbers = [0, 0, 0, 0, 0]
    if degree == 4:
        polynomial_numbers[4] = input("Enter value for []x^4 >>> ")
        while not is_float(polynomial_numbers[4]):
            polynomial_numbers[4] = input("Enter appropriate value for []x^4 >>> ")
    if degree >= 3:
        polynomial_numbers[3] = input("Enter value for []x^3 >>> ")
        while not is_float(polynomial_numbers[3]):
            polynomial_numbers[3] = input("Enter appropriate value for []x^3 >>> ")
    if degree >= 2:
        polynomial_numbers[2] = input("Enter value for []x^2 >>> ")
        while not is_float(polynomial_numbers[2]):
            polynomial_numbers[2] = input("Enter appropriate value for []x^2 >>> ")
    polynomial_numbers[1] = input("Enter value for []x >>> ")
    while not is_float(polynomial_numbers[1]):
        polynomial_numbers[1] = input("Enter appropriate value for []x >>> ")
    polynomial_numbers[0] = input("Enter final value >>> ")
    while not is_float(polynomial_numbers[0]):
        polynomial_numbers[0] = input("Enter appropriate final value >>> ")

    return [float(polynomial_numbers[0]), float(polynomial_numbers[1]), float(polynomial_numbers[2]),
            float(polynomial_numbers[3]), float(polynomial_numbers[4])]


def circle_centre_input(x, y):
    circle_centre = [0, 0]
    circle_centre[0] = x
    circle_centre[1] = y
    return circle_centre


def trigonometric_function_input(trigonometric_function):
    """
    selection of which type of trigonometric function they
    want to select (e.g. sin, cos, tan)
    """
    while trigonometric_function not in ["SIN", "COS", "TAN"]:
        """
        validation loop, making sure they pick a valid trigonometric function
        """
        trigonometric_function = input("Please enter appropriate function (sin, cos or tan) >>> ").upper()
    return trigonometric_function


def log_inputs(log_type):
    """
    what type of log graph they want to plot
    """
    while log_type not in ["LOG", "LN", "E"]:
        log_type = input("Please enter an appropriate function (Log, ln or e) >>> ").upper()
    return log_type


def is_float(input):
    try:
        return -1000 < float(input) < 1000
    except ValueError:
        return False


def is_int(input):
    try:
        return 1 <= int(input) <= 4
    except ValueError:
        return False


graph_repeat_input = True

while graph_repeat_input:
    reload(equations)
    equation_input = input("Enter what type of graph you want (Polynomial, Circle, Trigonometric, log) >>> ").upper()

    if equation_input == "POLYNOMIAL" or equation_input == "P":
        polynomial_degree = input("Degree of polynomial (1-4) >>> ")
        while not is_int(polynomial_degree):
            polynomial_degree = input("Enter appropriate degree of polynomial (1-4) >>> ")
        if axis_bool:
            equation_coordinates = equations.Polynomial(equations.Axis(-10, 10, -10, 10),
                                                        polynomial_input(int(polynomial_degree))).points
        graph_repeat_input = False

    elif equation_input == "CIRCLE" or equation_input == "C":
        circle_x = input("Enter the x coordinate for centre of circle >>> ")
        while not is_float(circle_x):
            circle_x = input("Enter the x coordinate for centre of circle >>> ")
        circle_y = input("Enter the y coordinate for the centre of circle >>> ")
        while not is_float(circle_y):
            circle_y = input("Enter the y coordinate for the centre of circle >>> ")
        inputted_radius = input("Enter the radius of the circle >>> ")
        while not is_float(inputted_radius):
            inputted_radius = input("Enter the radius of the circle >>> ")
        if axis_bool:
            equation_coordinates = equations.Circle(equations.Axis(-10, 10, -10, 10),
                                                    circle_centre_input(float(circle_x), float(circle_y)),
                                                    float(inputted_radius)).points
        graph_repeat_input = False

    elif equation_input == "TRIGONOMETRIC" or equation_input == "TRIG" or equation_input == "T":
        trigonometric_input = input("Enter chosen Trigonometric function >>> ").upper()
        trigonometric_input = trigonometric_function_input(trigonometric_input)
        x_coeffcieint_input = float(input("Enter appropriate coefficient of x f(kx) >>> "))
        while not is_float(x_coeffcieint_input):
            x_coeffcieint_input = float(input("Enter coefficient of x f(kx) >>> "))
        function_coefficient_input = float(input("Enter coefficient of function kf(x) >>> "))
        while not is_float(function_coefficient_input):
            function_coefficient_input = float(input("Enter appropriate coefficient of function kf(x) >>> "))
        if axis_bool:
            equation_coordinates = equations.Trigonometric(equations.Axis(-10, 10, -10, 10),
                                                           trigonometric_input,
                                                           float(x_coeffcieint_input),
                                                           float(function_coefficient_input)).points
        graph_repeat_input = False

    elif equation_input == "LOG" or equation_input == "L":
        log_input = input("Log, ln or e graph? >>> ").upper()
        log_input = log_inputs(log_input)
        if log_input == "LOG":
            log_base = input("Enter base of log >>> ")
            while not is_float(log_base):
                log_base = input("Enter appropriate base of log >>> ")
        else:
            log_base = 0
        if axis_bool:
            equation_coordinates = equations.Logarithm(equations.Axis(-10, 10, -10, 10), log_input,
                                                       float(log_base)).points
        graph_repeat_input = False
    else:
        print("Please enter a valid graph")
