def interpreter():
    x = int(input("Enter any number: "))
    y = input("Choose an operator (+, -, *, /): ")
    z = int(input("Enter another number: "))


    if y == "*":
            print(f"The answer is {x * z:.1f}")
    elif y == "+":
            print(f"The answer is {x + z:.1f}")
    elif y == "-":
            print(f"The answer is {x - z:.1f} ")
    elif y == "/":
        if z == 0:
            z = int(input("You cannot devide by zero, try another number: "))
        print(f"The answer is {x / z:.1f} ")
    else:
            print("Oops! That is not stored in my memory.")
interpreter()
