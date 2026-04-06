"""
# Module 8 : Portfolio Milestone
# Online Shopping Cart
# Jeremy Matthews
# Colorado State University Global
# CSC500– Principles of Programming
# Dr. Douglas Mujeye
# Due Date: 04/05/26
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
# 
# Step 7:
# In the main section of your code, prompt the user for a customer's name and today's date. 
# Output the name and date. Create an object of type ShoppingCart.
# 
# Step 8:
# Implement Add item to cart menu option.
# 
# Step 9:
# Implement remove item menu option.
# 
# Step 10:
# Implement Change item quantity menu option. Hint: Make new ItemToPurchase object before using ModifyItem() method.
"""

import math
from datetime import date, datetime


class ShoppingCartError(Exception):
    """Base exception for shopping cart operations."""
    pass


class InvalidItemError(ShoppingCartError):
    """Raised when an invalid item is provided to the shopping cart."""
    pass


class CartOperationError(ShoppingCartError):
    """Raised when a cart operation fails unexpectedly."""
    pass


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
        if not value.strip() and value != "none":
            raise ValueError("Item name cannot be empty.")
        self._item_name = value

    @property
    def item_price(self):
        return self._item_price

    @item_price.setter
    def item_price(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Item price must be a number.")
        if math.isnan(value) or math.isinf(value):
            raise ValueError("Price must be a finite number.")
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
        if not value.strip() and value != "none":
            raise ValueError("Item description cannot be empty.")
        self._item_description = value

    def __str__(self):
        return f"{self.item_name} - {self.item_description} (Qty: {self.item_quantity}, ${self.item_price:.2f} each)"

    def __repr__(self):
        return (f"ItemToPurchase(item_name={self.item_name!r}, item_price={self.item_price}, "
                f"item_quantity={self.item_quantity}, item_description={self.item_description!r})")

    def print_item_cost(self):
        total = round(self.item_price * self.item_quantity, 2)
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${total:.2f}")


class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    @property
    def customer_name(self):
        return self._customer_name

    @customer_name.setter
    def customer_name(self, value):
        if not isinstance(value, str):
            raise TypeError("Customer name must be a string.")
        if not value.strip():
            raise ValueError("Customer name cannot be empty.")
        self._customer_name = value

    @property
    def current_date(self):
        return self._current_date

    @current_date.setter
    def current_date(self, value):
        if not isinstance(value, str):
            raise TypeError("Current date must be a string.")
        if not value.strip():
            raise ValueError("Current date cannot be empty.")
        self._current_date = value

    def __str__(self):
        return f"{self.customer_name}'s Shopping Cart - {self.current_date} ({self.get_num_items_in_cart()} items, ${self.get_cost_of_cart():.2f})"

    def __repr__(self):
        return (f"ShoppingCart(customer_name={self.customer_name!r}, "
                f"current_date={self.current_date!r}, cart_items={self.cart_items!r})")

    def _find_item(self, item_name):
        """Return the first item matching item_name (case-insensitive), or None."""
        return next((item for item in self.cart_items if item.item_name.lower() == item_name.lower()), None)

    def add_item(self, item):
        if not isinstance(item, ItemToPurchase):
            raise InvalidItemError("Only ItemToPurchase objects can be added to the cart.")
        if self._find_item(item.item_name):
            raise CartOperationError(f"'{item.item_name}' already in cart. Use change quantity option to modify.")
        self.cart_items.append(item)
        print(f"'{item.item_name}' added to cart.")

    def remove_item(self, item_name):
        if not isinstance(item_name, str):
            raise InvalidItemError("Item name must be a string.")
        found = self._find_item(item_name)
        if not found:
            raise CartOperationError("Item not found in cart. Nothing removed.")
        self.cart_items.remove(found)
        print(f"'{item_name}' removed from cart.")

    def modify_item(self, modified_item, quantity_explicitly_set=False):
        if not isinstance(modified_item, ItemToPurchase):
            raise InvalidItemError("Only ItemToPurchase objects can be used to modify cart items.")
        found = self._find_item(modified_item.item_name)
        if not found:
            raise CartOperationError("Item not found in cart. Nothing modified.")
        if modified_item.item_description.lower() != "none":
            found.item_description = modified_item.item_description
        if not math.isclose(modified_item.item_price, 0.0):
            found.item_price = modified_item.item_price
        if modified_item.item_quantity != 0 or quantity_explicitly_set:
            found.item_quantity = modified_item.item_quantity
        print(f"'{found.item_name}' has been modified.")

    def get_num_items_in_cart(self):
        return sum(item.item_quantity for item in self.cart_items)

    def get_cost_of_cart(self):
        return round(sum(item.item_price * item.item_quantity for item in self.cart_items), 2)

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
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
        else:
            print("Item Descriptions")
            for item in self.cart_items:
                print(f"{item.item_name}: {item.item_description}")


def get_item_input():
    """Prompt user for all item fields and return a populated ItemToPurchase."""
    new_item = ItemToPurchase()

    while True:
        try:
            name = input("Enter the item name:\n").strip()
            if name.lower() == "none":
                print("'none' is a reserved name. Please choose a different item name.")
                continue
            new_item.item_name = name
            break
        except ValueError:
            print("Item name cannot be empty.")

    while True:
        try:
            description = input("Enter the item description:\n").strip()
            if description.lower() == "none":
                print("'none' is a reserved description. Please enter a valid description.")
                continue
            new_item.item_description = description
            break
        except ValueError:
            print("Item description cannot be empty.")

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
    if not isinstance(cart, ShoppingCart):
        raise TypeError("print_menu requires a ShoppingCart object.")

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
                try:
                    cart.add_item(new_item)
                except CartOperationError as e:
                    print(e)

            elif choice == "r":
                print("\nREMOVE ITEM FROM CART")
                while True:
                    item_name = input("Enter name of item to remove:\n").strip()
                    if item_name:
                        break
                    print("Item name cannot be empty.")
                try:
                    cart.remove_item(item_name)
                except CartOperationError as e:
                    print(e)

            elif choice == "c":
                print("\nCHANGE ITEM QUANTITY")
                modified_item = ItemToPurchase()

                while True:
                    try:
                        name = input("Enter the item name:\n").strip()
                        if name.lower() == "none":
                            print("'none' is a reserved name. Please enter a valid item name.")
                            continue
                        modified_item.item_name = name
                        break
                    except ValueError:
                        print("Item name cannot be empty.")

                while True:
                    try:
                        modified_item.item_quantity = int(input("Enter the new quantity:\n"))
                        break
                    except (ValueError, TypeError):
                        print("Please enter a valid, non-negative integer for the quantity.")

                try:
                    cart.modify_item(modified_item, quantity_explicitly_set=True)
                except CartOperationError as e:
                    print(e)

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
    try:
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

    except ShoppingCartError as e:
        print(f"\nShopping cart error: {e}")
    except (EOFError, KeyboardInterrupt):
        print("\nProgram interrupted. Exiting.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
