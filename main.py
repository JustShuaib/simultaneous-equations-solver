# SIMULTANEOUS EQUATION SOLVER
# EXAMPLE OF A SIMULATANEOUS EQUATION
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
        sign1 = input("Sign of eqn2(type in plus or minus): ")
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

    x1 = str(x1_coef) + "x"
    y1 = str(y1_coef) + "y"
    x2 = str(x2_coef) + "x"
    y2 = str(y2_coef) + "x"
    eqn1 = str(x1_y1_result)
    eqn2 = str(x2_y2_result)

    if sign01 == "plus":
        equation_1 = x1 + "+" + y1 + "=" + eqn1 + "----- (1)"

    elif sign01 == "minus":
        equation_1 = x1 + y1 + "=" + eqn1 + "----- (1)"

    if sign11 == "plus":
        equation_2 = x2 + "+" + y2 + "=" + eqn2 + "----- (2)"

    elif sign11 == "minus":
        equation_2 = x2 + y2 + "=" + eqn2 + "----- (1)"


    print("\n")
    print("Your simultaneous equation is: ")
    print(equation_1)
    print(equation_2)
    print("Solving simultaneous equation...")

    # USING ELIMINATION METHOD IF EITHER X1, X2 OR Y1, Y2 HAVE SAME COEFFICIENT

    # if y1_coef == y2_coef:


linear_simultaneous_equation()