print("Enter names. When you're done, press Ctrl+D then Enter.")
names = []
try:
    while True:
        name = input("Name: ")
        if name.strip():
            names.append(name.strip())
except EOFError:
        pass
if len(names) == 1:
    message = f"Adieu, {names[0]}"
elif len(names) == 2:
    message = f"Adieu, {names[0]} and {names[1]}"
else:
    message = "Adieu, adieu, to " + ", ".join(names[:-1]) + f", and {names[-1]}"
print("\n" + message)

