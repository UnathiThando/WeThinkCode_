def fuel():
    try:
        x = int(input("Enter the numerator: "))
        y = int(input("Enter the denominator: "))
        if x > 0 and y > 1:
            fraction = x / y
            percentage = fraction * 100
        elif y == 0:
            print("You cannot divide by 0")
        elif percentage < 1:
                print("E")
        elif percentage >= 99:
                print("F")
        else:
                print(f"Your tank is {round(percentage)}%")
    except ValueError:
        print("Only enter numbers")

fuel()
