"""
# Input budget

budget = float(input("Please input your total budget for spending: "))

# Request Item name and price

item_name = input("Please input requested item: ")
item_price = float(input("Please input item price: "))

# Subtract item to budget, display remaining budget

print(f"You have brought a {item_name} for {item_price}. Your remaining budget is {item_price - budget}.")
"""

budget = float(input("Please input your total budget for spending: "))

def budgetbuying():
    global budget
    global item_price
    item_name = input("Please input requested item: ")
    item_price = float(input("Please input item price: "))
    budget = budget - item_price
    def end1():
        global end
        global budget
        end = input("Do you wish to stop buying?: ")

        if end == "yes":
            print("Goodbye!")
            budget = 0

        elif end == "no":
            budgetbuying()

        else:
            print("How did we get here?")

    if budget > item_price:
        print(f"You have brought a {item_name} for {item_price}. Your remaining budget is {budget}.")
        end1()
        item_name = input("Please input requested item: ")
        item_price = float(input("Please input item price: "))
    
    elif budget < item_price:
        print("You do not have enough money to buy this")
        end1()

    else:
        print("How did we get here?")



while budget >= 0:
    budgetbuying()