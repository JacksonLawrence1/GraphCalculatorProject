import equations
from importlib import reload

axis_input_repeat = True

axis = equations.Axis(-10, 10, -10, 10)

while axis_input_repeat:
    try:
        axis_range = int(input("Enter range for x axis: "))
    except ValueError:
        print("Unknown input, please enter valid number")
    else:
        if (axis_range % 10) != 0:
            print("Must be a multiple of 10")
        elif axis_range > 1000:
            print("Too large")
        elif axis_range < 10 and axis_range > 0:
            print("Too small")
        elif axis_range < 0:
            print("Cannot be negative")
        else:
            reload(equations)
            axis = equations.Axis(-axis_range, axis_range, -axis_range, axis_range)
            axis_input_repeat = False
