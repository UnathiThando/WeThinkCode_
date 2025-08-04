coin= int(input("Insert a coin: "))
# while coin in (5, 25 ,):
#     print(f"Amount Due {50-coin}")
#     break
#     if coin == 50:
#         print(f"Change owed {50-coin}")
# else:
#     print("Money not accepted")
    
if coin in (5, 25, 50):
    if coin == 50:
        print("Change owed: 0")
    else:
        print(f"Amount Due: {50 - coin}")
else:
    print("Money not accepted")