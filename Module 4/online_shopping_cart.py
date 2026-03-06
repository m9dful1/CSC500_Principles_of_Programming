"""
# Module 4 : Portfolio Milestone
# Online Shopping Cart
# 
# Step 1: Build the ItemToPurchase class with the following specifications:
# 
# Attributes
# item_name (string)
# item_price (float)
# item_quantity (int)
# Default constructor
# Initializes item's name = "none", item's price = 0, item's quantity = 0
# Method
# print_item_cost()
# 
# Step 2: In the main section of your code, prompt the user for two items and create two objects of the ItemToPurchase class.
# 
# Step 3: Add the costs of the two items together and output the total cost.
"""

class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0.0
        self.item_quantity = 0

    def print_item_cost(self):
        total = self.item_price * self.item_quantity


if __name__ == "__main__":
    # Item 1
    print("Item 1")
    item1 = ItemToPurchase()
    while True:
        item1.item_name = input("Enter the item name:\n").strip()
        if item1.item_name:
            break
        print("Item name cannot be empty.")
    while True:
        try:
            item1.item_price = float(input("Enter the item price:\n"))
            if item1.item_price < 0:
                print("Price cannot be negative.")
                continue
            break
        except ValueError:
            print("Please enter a valid number for the price.")
    while True:
        try:
            item1.item_quantity = int(input("Enter the item quantity:\n"))
            if item1.item_quantity < 0:
                print("Quantity cannot be negative.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer for the quantity.")

    print()

    # Item 2
    print("Item 2")
    item2 = ItemToPurchase()
    while True:
        item2.item_name = input("Enter the item name:\n").strip()
        if item2.item_name:
            break
        print("Item name cannot be empty.")
    while True:
        try:
            item2.item_price = float(input("Enter the item price:\n"))
            if item2.item_price < 0:
                print("Price cannot be negative.")
                continue
            break
        except ValueError:
            print("Please enter a valid number for the price.")
    while True:
        try:
            item2.item_quantity = int(input("Enter the item quantity:\n"))
            if item2.item_quantity < 0:
                print("Quantity cannot be negative.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer for the quantity.")

    print()

    # Output total cost
    total_cost = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)

    print("TOTAL COST")
    item1.print_item_cost()
    item2.print_item_cost()
    print(f"\nTotal: ${total_cost:.2f}")