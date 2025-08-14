from collections import Counter
def grocery():
    print("Enter your items, when you are done press ctrl d")
    items = []
    try:
        while True:
            grocery_list = input("Enter your items: ")
            if grocery_list.strip() == "":
                continue
            items.extend(grocery_list.lower().split())
    except EOFError:
        pass
    total_items = Counter(items)
    for string in sorted(total_items):
        print(f"{total_items[string]} {string.upper()}")
grocery() 