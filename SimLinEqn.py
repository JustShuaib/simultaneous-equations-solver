# SIMULTANEOUS EQUATION SOLVER
# EXAMPLE OF A SIMULTANEOUS EQUATION
# x + y = 8
# 2x + 5y = 14
# Find x and y
def linear_simultaneous_equation():
    # sign00 is the sign of the first coefficient in equation_1
    # sign01 is the sign of the second coefficient in equation_1
    # sign0 is the sign of the result of equation_1
    # sign10 is the sign of the first coefficient in equation_2
    # sign11 is the sign of the second coefficient in equation_2
    # sign1 is the sign of the result in equation_2

    while True:
        sign00 = input("Sign of the first coefficient in eqn1 (type in plus or minus): ")
        sign00 = sign00.lower()
        if sign00 == "plus":
            break
        elif sign00 == "minus":
            break
        else:
            print("Sign not valid")

    while True:
        try:
            x1_coef = int(input("Type in the coefficient of x1 here: "))
            if sign00 == 'minus':
                x1_coef = -x1_coef
            break
        except ValueError as e:
            print("Only numbers allowed")

    while True:
        sign01 = input("Sign of the second coefficient in eqn1(type in plus or minus): ")
        sign01 = sign01.lower()
        if sign01 == "plus":
            break
        elif sign01 == "minus":
            break
        else:
            print("Sign not valid")

    while True:
        try:
            y1_coef = int(input("Type in the coefficient of y1 here: "))
            if sign01 == 'minus':
                y1_coef = -y1_coef
            break
        except ValueError as e:
            print("Only numbers allowed")
    while True:
        sign0 = input("Sign of the result in eqn1(type in plus or minus): ")
        sign0 = sign0.lower()
        if sign0 == "plus":
            break
        elif sign0 == "minus":
            break
        else:
            print("Sign not valid")

    while True:
        try:
            x1_y1_result = int(input("Type in the result of equation 1 here: "))
            if sign0 == 'minus':
                x1_y1_result = -x1_y1_result
            break
        except ValueError as e:
            print("Only numbers allowed")

    while True:
        sign10 = input("Sign of the first coefficient in eqn2 (type in plus or minus): ")
        sign10 = sign10.lower()
        if sign10 == "plus":
            break
        elif sign10 == "minus":
            break
        else:
            print("Sign not valid")

    while True:
        try:
            x2_coef = int(input("Type in the coefficient of x2 here: "))
            if sign10 == "minus":
                x2_coef = -x2_coef
            break
        except ValueError as e:
            print("Only numbers allowed")

    while True:
        sign11 = input("Sign of the second coefficient in eqn2 (type in plus or minus): ")
        sign11 = sign11.lower()
        if sign11 == "plus":
            break
        elif sign11 == "minus":
            break
        else:
            print("Sign not valid")

    while True:
        try:
            y2_coef = int(input("Type in the coefficient of y2 here: "))
            if sign11 == "minus":
                y2_coef = -y2_coef
            break
        except ValueError as e:
            print("Only numbers allowed")

    while True:
        sign1 = input("Sign of the result in eqn2(type in plus or minus): ")
        if sign1 == "plus":
            break
        elif sign1 == "minus":
            break
        else:
            print("Sign not valid")

    while True:
        try:
            x2_y2_result = int(input("Type in the result of equation 2 here: "))
            if sign1 == 'minus':
                x2_y2_result = -x2_y2_result
            break
        except ValueError as e:
            print("Only numbers allowed")

    # converting the integers to strings so the equations can be printed
    x1_show = str(x1_coef) + "x"
    y1_show = str(y1_coef) + "y"
    x2_show = str(x2_coef) + "x"
    y2_show = str(y2_coef) + "x"
    eqn1_show = str(x1_y1_result)
    eqn2_show = str(x2_y2_result)

    # printing out the equations for confirmation
    if sign01 == "plus":
        equation_1 = x1_show + "+" + y1_show + "=" + eqn1_show + "----- (1)"
    elif sign01 == "minus":
        equation_1 = x1_show + y1_show + "=" + eqn1_show + "----- (1)"
    if sign11 == "plus":
        equation_2 = x2_show + "+" + y2_show + "=" + eqn2_show + "----- (2)"
    elif sign11 == "minus":
        equation_2 = x2_show + y2_show + "=" + eqn2_show + "----- (2)"

    print("\n")
    print("Your simultaneous equation is: ")
    print(equation_1)
    print(equation_2)
    print("Solving simultaneous equation...")
    # USING ELIMINATION METHOD

    # creating a new variable to convert the coefficients of each variable to positive
    # to enable for comparison of the coefficients of the variables
    if y1_coef < 0:
        y1_coef_positive = -1 * y1_coef
    else:
        y1_coef_positive = y1_coef
    if y2_coef < 0:
        y2_coef_positive = -1 * y2_coef
    else:
        y2_coef_positive = y2_coef
    if x1_coef < 0:
        x1_coef_positive = -1 * x1_coef
    else:
        x1_coef_positive = x1_coef
    if x2_coef < 0:
        x2_coef_positive = -1 * x2_coef
    else:
        x2_coef_positive = x2_coef

    # using elimination method if the coefficients of variable y are the same but with
    # different signs e.g + and -
    if y1_coef_positive == y2_coef_positive:
        if sign01 != sign11:
            # adding the coefficients of the variable x together after y has been eliminated
            # from the equation
            x_coef = x1_coef + x2_coef

            # Adding the results of both equations.
            result = x1_y1_result + x2_y2_result
            # dividing the added result by the added coefficients of x to get the value of x
            x = result / x_coef
            print(f"X = {x}")

            # FINDING THE VALUE OF Y

            # Multiplying the coefficient of x in equation 1 by the value of x gotten from the
            # equation.
            x_new_eqn = x1_coef * x

            # this block of code checks if the new number gotten from the multiplication of x and it's coefficient
            # is negative. In maths, when a number is taken to the other side of an "=", the sign is inverted from
            # either positive to negative. Since the resulting value of x_new_eqn is negative, it is multiplied by
            # "-" to convert it to positive as seen in (-x_new_eqn) which is just short of -1 * x_new_eqn.
            if x_new_eqn < 0:
                new_result = x1_y1_result + (-x_new_eqn)
            else:
                # if x_new_eqn is positive, it is subtracted from the equation value of eqn(1)
                new_result = x1_y1_result - x_new_eqn
            y = new_result / y1_coef
            print(f"Y = {y}")

        # This is the code that is executed when the signs of the coefficients of y in both equations
        # are the same.
        elif sign01 == sign11:
            # Subtracting the coefficients of x in both equations and the results of both equations after y has been
            # eliminated from the equation.
            x_coef = x2_coef - x1_coef
            # Subtracting the results of both equations.
            result = x2_y2_result - x1_y1_result
            # Dividing the result of the equation by the coefficient of x to get the value of x.
            x = result / x_coef
            print(f"X= {x}")

            x_new_eqn = x1_coef * x
            if x_new_eqn < 0:
                new_result = x1_y1_result + (-x_new_eqn)
            else:
                new_result = x1_y1_result - x_new_eqn
            y = new_result / y1_coef
            print(f"Y = {y}")

    elif x1_coef_positive == x2_coef_positive:
        if sign00 != sign10:
            y_coef = y1_coef + y2_coef
            result = x1_y1_result + x2_y2_result
            y = result / y_coef
            print(f"Y = {y}")
            y_new_eqn = y1_coef * y
            if y_new_eqn < 0:
                new_result = x1_y1_result + (-y_new_eqn)
            else:
                new_result = x1_y1_result - y_new_eqn
            x = new_result / x1_coef
            print(f"X = {x}")

        elif sign00 == sign10:
            y_coef = y2_coef - y1_coef
            result = x2_y2_result - x1_y1_result
            y = result / y_coef
            print(f"Y = {y}")

            y_new_eqn = y1_coef * y
            if y_new_eqn < 0:
                new_result = x1_y1_result + (-y_new_eqn)
            else:
                new_result = x1_y1_result - y_new_eqn
            x = new_result / x1_coef
            print(f"X = {x}")

    # USING SUBSTITUTION METHOD
    # This is used when no coefficients of either variables are found to be the same

    elif x1_coef_positive == 1:
        # during the substitution method, after making x the subject of equation 1
        # the num variable is the multiplication of the coefficient of x in equation 2
        # and the first value "7" using a sample equation (x = 7 + 5y)

        # num_y1 is the multiplication of x_coef in equation 2 and the coefficient of y in the
        # sample equation above

        # num_y then becomes the addition of num_y1 and the coefficient of y in equation 2
        # which is also known as the addition of like terms (y in this scenario)
        num = x2_coef * x1_y1_result
        num_y1 = x2_coef * -y1_coef
        num_y = num_y1 + y2_coef
        num_y = -num_y
        new_result = num - x2_y2_result
        y = new_result / num_y
        print(f"Y = {y}")

        x = x1_y1_result - (y1_coef * y)
        print(f"X = {x}")

    elif y1_coef_positive == 1:
        num = y2_coef * x1_y1_result
        num_x1 = y2_coef * -x1_coef
        num_x = num_x1 + x2_coef
        num_x = -num_x
        new_result = num - x2_y2_result
        x = new_result / num_x
        print(f"X = {x}")

        y = x1_y1_result - (x1_coef * x)
        print(f"Y = {y}")

    elif x2_coef_positive == 1:
        num = x1_coef * x2_y2_result
        num_y1 = x1_coef * -y2_coef
        num_y = num_y1 + y1_coef
        num_y = -num_y
        new_result = num - x1_y1_result
        y = new_result / num_y
        print(f"Y = {y}")

        x = x2_y2_result - (y2_coef * y)
        print(f"X = {x}")

    elif y2_coef_positive == 1:
        num = y1_coef * x2_y2_result
        num_x1 = y1_coef * -x2_coef
        num_x = num_x1 + x1_coef
        num_x = -num_x
        new_result = num - x1_y1_result
        x = new_result / num_x
        print(f"X = {x}")

        y = x2_y2_result - (x2_coef * x)
        print(f"Y = {y}")

    else:
        x_upper = ((x1_y1_result * y2_coef) - (x2_y2_result * y1_coef))
        x_lower = ((x1_coef * y2_coef) - (x2_coef * y1_coef))
        x = x_upper / x_lower
        print(f"X = {x}")

        y = (x1_y1_result - (x1_coef * x)) / y1_coef
        print(f"Y = {y}")


linear_simultaneous_equation()
