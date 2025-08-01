def greet():
    greet= input("Hey! How can I help you today?: ")
    if greet.lower() == "hello":
        print("$0")
    elif greet[0] == "h" and greet != "hello":
        print("$20")
    else:
        print("$100")
greet()
    