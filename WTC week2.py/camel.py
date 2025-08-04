def camel():
    text = input("Enter a text: ")
    if len(text) >= 2:
        print(f"snake_case: {text.replace(' ', '_')}")
    # elif len(text) > 1:
        words = text.split()
        camel = words[0].lower() + ''.join(word.capitalize() for word in words[1:])
        print(f"camelCase: {camel}")
    elif len(text) > 0:
        print(f"snake_case: {text.lower()}")
        print(f"camelCase: {text.lower()}")
camel()