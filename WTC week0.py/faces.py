def convert(text):
    return text.replace("(:", "😊").replace("):", "☹") #Do not use print but return

def main():
    string = input("Enter a message with (: or ): ")
    # print(f"Hello stranger, {string}")
    message = convert(string) # Here you are calling the prev function to be excetuted in our string
    print(f"Hello stranger, {message}")

main()