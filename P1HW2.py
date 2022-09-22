# A brief description of the project
# 9/22/22
# CTI-110 P1HW2 - Travel Expense
# Angel ramos
#
print("This program calculates and displays travel expenses")
print()
initial_budget = float(input("How much do we have?:",))
print()
destination = input("Where we going?:")
print()
gas = float(input("Gas budget?:"))
print()
accommodations = float(input("accommodations expenses"))
print()
food = float(input("food cost"))
reminder = float(initial_budget - gas - accommodations - food)
print()
print("------------Travel Expenses----------")
print("The destination: ", destination)
print("what do we hav: ", initial_budget)
print()
print("Gas budget:", gas)
print("accommodations:", accommodations)
print("food:", food)
print()
print("Here is  what's left:", reminder)
# Ask user input for (initial budget, destination, gas, accommodations , food)
# Display the user's input for each variable.
# use the input to calculate the remaining budget after expenses.






