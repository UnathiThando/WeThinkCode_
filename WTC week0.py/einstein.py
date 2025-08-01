# In a file called einstein.py, implement a program in Python that prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.
mass= int(input("Enter mass in kg: "))
c=  300000000
Energy= mass*c**2
print(f"Energy is equal to {Energy}J")