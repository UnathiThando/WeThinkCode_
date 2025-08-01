def main():
    time = float(input("What time is it? "))  
    convert(time)

def convert(time):
    if 7.0 <= time <= 9.0:
        print("breakfast time")
    elif 12.0 <= time <= 13.0:
        print("lunch time")
    elif 18.0 <= time <= 20.0:
        print("dinner time")
    else:
        print("Not a meal time")

if __name__ == "__main__":
    main()
