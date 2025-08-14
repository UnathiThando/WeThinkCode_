import random

def main():
    level=get_level
    

def get_level():
    while True:
        level=int(input("Level: "))
        if level < 1 and get_level >3:
            print("Level must be 1,2 or 3")
            level=int(input("Level: "))

def generate_integer(level):
    if level < 1 and level >3:
        print("Level must be 1,2 or 3")
        level=int(input("Level: "))


if __name__ == "__main__":
    main()