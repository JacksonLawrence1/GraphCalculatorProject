def polynomial_input():
    """
    selection of which graph they want to visualize
    e.g. if degree is 2 then graph will be set to a quadratic
    """
    degree = float(input("Degree of polynomial (1-4) >>> "))
    while degree < 1 or degree > 4:  # validation loop so user must select 1, 2, 3 or 4
        degree = float(input("Please enter an appropriate value (1-4) >>> "))
    polynomial_numbers = [0, 0, 0, 0, 0]
    if degree == 4:
        polynomial_numbers[4] = float(input("Enter value for []x^4 >>> "))
    if degree >= 3:
        polynomial_numbers[3] = float(input("Enter value for []x^3 >>> "))
    if degree >= 2:
        polynomial_numbers[2] = float(input("Enter value for []x^2 >>> "))
    polynomial_numbers[1] = float(input("Enter value for []x >>> "))
    polynomial_numbers[0] = float(input("Enter final value >>> "))

    return polynomial_numbers


def circle_centre_input():
    circle_centre = [0, 0]
    circle_centre[0] = float(input("Enter the x coordinate for centre of circle >>> "))
    circle_centre[1] = float(input("Enter the y coordinate for the centre of circle >>> "))
    return circle_centre


def circle_radius_input():
    circle_radius = float(input("Enter the radius of the circle >>> "))
    return circle_radius


def trigonometric_function_input():
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


def log_inputs():
    """
    what type of log graph they want to plot
    """
    log_input = [input("Log, ln or e graph? >>> ").upper(), 0]
    while log_input[0] not in ["LOG", "LN", "E"]:
        log_input = input("Please enter an appropriate function (Log, ln or e) >>> ").upper()
    if log_input[0] == "LOG":
        log_input[1] = float(input("Please enter the base for the log you chosen >>> "))
    return log_input
