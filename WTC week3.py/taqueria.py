price_list= {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
total_price = 0
while True:
    place_order = input("Place your order (press d to exit): ")
    if place_order == "d":
        break
    elif place_order in price_list:
        total_price += price_list[place_order]
        print(f"Added {place_order}. Total price is R{total_price:.2f}")
    else:
        print("Item not available.")
print(f"Total Price : R{total_price:.2f}")
