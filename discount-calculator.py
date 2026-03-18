# Discount calculator
# Author: Fauzan Hanandito

# -----------------------------------------------------------------

### Part 1: Number type checker

# Will check if the input is a float.
def is_float(s):
    
    # Try to convert the input to float.
    try:
        float(s)

        # If it is, return True.    
        return True

    # If it is not, return False.
    except ValueError:
        return False

# -----------------------------------------------------------------

### Part 2: Price ###

# Until the price is valid, we will keep asking for it.
while True:

    # Get the price from the user.
    price = input("Enter the price: ")

    # Check if the input exists
    if price == "":
        print("Price must be not empty!")

    # Check if the type of data for the price is correct.
    elif not is_float(price):
        print("Price must be a valid number!")

    # Check if the price is greater than 0.
    elif float(price) < 0.0:
        print("Price must be no less than 0!")

    # If all correct, move on. 
    else:
        price = float(price)
        break

# -----------------------------------------------------------------

### Part 2: Discount ###

# Until the discount is valid, we will keep asking for it.
while True:

    # Get the discount from the user.
    discount = input("Enter the discount in percentage (0-100): ")

    # Check if the input exists
    if discount == "":
        print("Discount must be not empty!")

    # Check if the type of data for the discount is correct.
    if not is_float(discount):
        print("Discount must be a valid number!")

    # Check if the discount is no more than 0 and no less than 100.
    elif float(discount) > 100.0 or float(discount) < 0.0:
        print("Discount must be no less than 0 and no more than 100!")

    # If all correct, move on and 
    else:
        discount = float(discount)
        break

# -----------------------------------------------------------------

### Part 3: Calculation ###

# Remember that discounted price is the price minus the discount times the price.
discounted_price = price * (1 - discount / 100.0)

# Then print it, and we are done.
print(f"Discounted price = {discounted_price:.2f}")

# -----------------------------------------------------------------

### Part 4 (Optional): flavor text ###

# Flavor text if needed.
print("Thank you for using this program!")