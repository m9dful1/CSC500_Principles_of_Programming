"""
# Part 1:
# Write a program that calculates the total amount of a meal purchased at a restaurant. 
# The program should ask the user to enter the charge for the food and then 
# calculate the amounts with an 18 percent tip and 7 percent sales tax. 
# Display each of these amounts and the total price.
"""
try:
    # Get the food charge from the user
    food_charge = float(input("Enter the charge for the food: $"))

    # Validate that the charge is not negative
    if food_charge < 0:
        print("Error: Food charge cannot be negative.")
    else:
        # Calculate tip and tax
        tip = food_charge * 0.18
        tax = food_charge * 0.07

        # Calculate total
        total = food_charge + tip + tax

        # Display the results
        print(f"Food Charge:    ${food_charge:,.2f}")
        print(f"Tip (18%):      ${tip:,.2f}")
        print(f"Sales Tax (7%): ${tax:,.2f}")
        print(f"Total:          ${total:,.2f}")

except ValueError:
    print("Error: Please enter a valid number for the food charge.")