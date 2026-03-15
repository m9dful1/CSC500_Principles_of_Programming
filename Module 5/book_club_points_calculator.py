"""
# Part 2:
# The CSU Global Bookstore has a book club that awards points to its students based on the number of books purchased each month. 
# The points are awarded as follows:
# 
# * If a customer purchases 0 books, they earn 0 points.
# * If a customer purchases 2 books, they earn 5 points.
# * If a customer purchases 4 books, they earn 15 points.
# * If a customer purchases 6 books, they earn 30 points.
# * If a customer purchases 8 or more books, they earn 60 points.
# Write a program that asks the user to enter the number of books that they have purchased this month and then display the number of points awarded.
"""

# ─────────────────────────────────────────
# CSU Global Bookstore - Book Club Points
# Calculates reward points based on the
# number of books purchased in a month.
# ─────────────────────────────────────────

books = input("Enter the number of books purchased this month: ")

# Validate input is a non-negative integer
if not books.isdigit():
    print("Please enter a valid non-negative whole number.")
else:
    books = int(books)

    if books >= 8:
        points = 60
    elif books >= 6:
        points = 30
    elif books >= 4:
        points = 15
    elif books >= 2:
        points = 5
    else:
        points = 0

    print(f"\nBooks purchased : {books}")
    print(f"Points awarded  : {points}")


"""**Sample outputs:**

# Input: 3
Books purchased : 3
Points awarded  : 5

# Input: 8
Books purchased : 8
Points awarded  : 60

# Input: 0
Books purchased : 0
Points awarded  : 0"""