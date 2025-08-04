def nutrition():
    fruits = {"apple": 130,"avocado": 50,"banana": 110,"cantaloupe": 50,"grapefruit": 60,"grapes": 90,"honeydew melon": 60,"orange": 80,"peach": 60,"pear": 100,"sweet cherries": 100,"tangerine": 50,}
    item= input("Enter fruit: ").lower()
    # for item in fruits:
    #     print(f"{item} is {fruits} calories")
    # else:
    #     print(f"{item} is not available")
    if item in fruits:
        print(f"Calories: {fruits[item]}")
    else:
        print("Fruit not available.")

nutrition()