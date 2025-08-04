def main():
    plate = input("Plate: ").lower()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
def is_valid(s):
    if s[0].isdigit() and s[1].isdigit():
        return False
    elif s[0] == '0':
        return False
    elif len(s) <= 6:
        return True
    return False
main()