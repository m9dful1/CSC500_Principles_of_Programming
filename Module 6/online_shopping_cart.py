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
#
# Step 4: Build the ShoppingCart class with the following data attributes and related methods.
# Note: Some can be method stubs (empty methods) initially, to be completed in later steps
#
# Parameterized constructor, which takes the customer name and date as parameters
# Attributes
# customer_name (string) - Initialized in default constructor to "none"
# current_date (string) - Initialized in default constructor to "January 1, 2020"
# cart_items (list)
# Methods
# add_item()
# Adds an item to cart_items list. Has parameter ItemToPurchase. Does not return anything.
# remove_item()
# Removes item from cart_items list. Has a string (an item's name) parameter. Does not return anything.
# If item name cannot be found, output this message: Item not found in cart. Nothing removed.
# modify_item()
# Modifies an item's description, price, and/or quantity. Has parameter ItemToPurchase. Does not return anything.
# If item can be found (by name) in cart, check if parameter has default values for description, price, and quantity.
# If not, modify item in cart.
# If item cannot be found (by name) in cart, output this message: Item not found in cart. Nothing modified.
# get_num_items_in_cart()
# Returns quantity of all items in cart. Has no parameters.
# get_cost_of_cart()
# Determines and returns the total cost of items in cart. Has no parameters.
# print_total()
# Outputs total of objects in cart.
# If cart is empty, output this message: SHOPPING CART IS EMPTY
# print_descriptions()
# Outputs each item's description.
#
# Step 5: In the main section of your code, implement the print_menu() function.
# print_menu() has a ShoppingCart parameter and outputs a menu of options to manipulate the shopping cart.
# Each option is represented by a single character. Build and output the menu within the function.
#
# If an invalid character is entered, continue to prompt for a valid choice.
# Hint: Implement Quit before implementing other options. Call print_menu() in the main() function.
# Continue to execute the menu until the user enters q to Quit.
#
# Step 6: Implement Output shopping cart menu option. Implement Output item's description menu option.
"""

import math
from datetime import date, datetime


class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0, item_description="none"):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, value):
        if not isinstance(value, str):
            raise TypeError("Item name must be a string.")
        self._item_name = value

    @property
    def item_price(self):
        return self._item_price

    @item_price.setter
    def item_price(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Item price must be a number.")
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self._item_price = float(value)

    @property
    def item_quantity(self):
        return self._item_quantity

    @item_quantity.setter
    def item_quantity(self, value):
        if not isinstance(value, int):
            raise TypeError("Item quantity must be an integer.")
        if value < 0:
            raise ValueError("Quantity cannot be negative.")
        self._item_quantity = value

    @property
    def item_description(self):
        return self._item_description

    @item_description.setter
    def item_description(self, value):
        if not isinstance(value, str):
            raise TypeError("Item description must be a string.")
        self._item_description = value

    def print_item_cost(self):
        total = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${total:.2f}")


class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def _find_item(self, item_name):
        """Return the first item matching item_name, or None."""
        return next((item for item in self.cart_items if item.item_name == item_name), None)

    def add_item(self, item):
        if self._find_item(item.item_name):
            print(f"'{item.item_name}' already in cart. Use change quantity option to modify.")
            return
        self.cart_items.append(item)

    def remove_item(self, item_name):
        found = self._find_item(item_name)
        if found:
            self.cart_items.remove(found)
            print(f"'{item_name}' removed from cart.")
        else:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self, modified_item):
        found = self._find_item(modified_item.item_name)
        if not found:
            print("Item not found in cart. Nothing modified.")
            return
        if modified_item.item_description != "none":
            found.item_description = modified_item.item_description
        if not math.isclose(modified_item.item_price, 0.0):
            found.item_price = modified_item.item_price
        if modified_item.item_quantity != 0:
            found.item_quantity = modified_item.item_quantity

    def get_num_items_in_cart(self):
        return sum(item.item_quantity for item in self.cart_items)

    def get_cost_of_cart(self):
        return sum(item.item_price * item.item_quantity for item in self.cart_items)

    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}")
        print()
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
        else:
            for item in self.cart_items:
                item.print_item_cost()
            print()
            print(f"Total: ${self.get_cost_of_cart():.2f}")

    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print()
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}")


def get_item_input():
    """Prompt user for all item fields and return a populated ItemToPurchase."""
    new_item = ItemToPurchase()

    while True:
        new_item.item_name = input("Enter the item name:\n").strip()
        if new_item.item_name:
            break
        print("Item name cannot be empty.")

    new_item.item_description = input("Enter the item description:\n").strip()

    while True:
        try:
            new_item.item_price = float(input("Enter the item price:\n"))
            break
        except ValueError:
            print("Please enter a valid, non-negative number for the price.")

    while True:
        try:
            new_item.item_quantity = int(input("Enter the item quantity:\n"))
            break
        except (ValueError, TypeError):
            print("Please enter a valid, non-negative integer for the quantity.")

    return new_item


def print_menu(cart):
    menu = (
        "\nMENU\n"
        "a - Add item to cart\n"
        "r - Remove item from cart\n"
        "c - Change item quantity\n"
        "i - Output items' descriptions\n"
        "o - Output shopping cart\n"
        "q - Quit\n"
    )

    try:
        while True:
            print(menu)
            choice = input("Choose an option:\n").strip().lower()

            if choice == "q":
                break

            elif choice == "a":
                print("\nADD ITEM TO CART")
                new_item = get_item_input()
                cart.add_item(new_item)

            elif choice == "r":
                print("\nREMOVE ITEM FROM CART")
                item_name = input("Enter name of item to remove:\n").strip()
                cart.remove_item(item_name)

            elif choice == "c":
                print("\nCHANGE ITEM QUANTITY")
                modified_item = ItemToPurchase()

                while True:
                    modified_item.item_name = input("Enter the item name:\n").strip()
                    if modified_item.item_name:
                        break
                    print("Item name cannot be empty.")

                while True:
                    try:
                        modified_item.item_quantity = int(input("Enter the new quantity:\n"))
                        break
                    except (ValueError, TypeError):
                        print("Please enter a valid, non-negative integer for the quantity.")

                cart.modify_item(modified_item)

            elif choice == "o":
                print("\nOUTPUT SHOPPING CART")
                cart.print_total()

            elif choice == "i":
                print("\nOUTPUT ITEMS' DESCRIPTIONS")
                cart.print_descriptions()

            else:
                print("Invalid option. Please choose a valid menu option.")
    except (EOFError, KeyboardInterrupt):
        print("\nExiting.")


if __name__ == "__main__":
    while True:
        customer_name = input("Enter customer's name:\n").strip()
        if customer_name:
            break
        print("Customer name cannot be empty.")

    while True:
        date_input = input("Enter today's date (MM/DD/YYYY) or press Enter for today's date:\n").strip()
        if not date_input:
            current_date = date.today().strftime("%B %d, %Y")
            break
        try:
            parsed_date = datetime.strptime(date_input, "%m/%d/%Y")
            current_date = parsed_date.strftime("%B %d, %Y")
            break
        except ValueError:
            print("Invalid date. Please use MM/DD/YYYY format (e.g., 01/01/2020).")

    print()
    print(f"Customer name: {customer_name}")
    print(f"Today's date: {current_date}")

    cart = ShoppingCart(customer_name, current_date)

    print_menu(cart)
