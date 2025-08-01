question= input("What is the Answer to the Great Question of Life, the Universe and Everything?")
if question == "42":
    print("Yes!")
elif question.lower() == "fourty two":
    print("Yes!")
elif question.lower() == "fourty-two":
    print("Yes!")
else:
    print("No!")