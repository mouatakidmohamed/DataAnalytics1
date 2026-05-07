# ============================================================
# File: Ex2A_tips.py
# Location: week-05/Ex2A_tips.py
# ============================================================

# Define known values
food_cost = 79.25
tax = 6.54
tip = 12.00

# Calculate the unknown
total_due = food_cost + tax + tip

# str() converts numbers into text/string.
# We use str() because Python cannot combine regular text with numbers directly.

# Original print statement:
# print("The total due is " + str(total_due))

print("Food cost is " + str(food_cost) + " and tax is " + str(tax))

# format(tip, ".2f") displays the tip with two digits after the decimal point.
# Since format() already returns a string, we do not need to use str() with it.
print("Tip is " + format(tip, ".2f"))

print("Total due is " + str(total_due))


# ============================================================
# File: net_worth.py
# Location: week-05/Ex2A_MathScripts/net_worth.py
# ============================================================

# Assets are things you own that have value.
cash = 1200
savings = 3500
car_value = 8000
personal_items = 1500

# Debts are money you owe.
credit_card_debt = 600
student_loan = 2500
car_loan = 3000

# Calculate totals
total_assets = cash + savings + car_value + personal_items
total_debts = credit_card_debt + student_loan + car_loan
net_worth = total_assets - total_debts

# Display results
print("Your total assets are " + str(total_assets))
print("Your total debts are " + str(total_debts))
print("Your net worth is " + str(net_worth))


# ============================================================
# File: area_of_rectangle.py
# Location: week-05/Ex2A_MathScripts/area_of_rectangle.py
# ============================================================

# Formula: area = side_a * side_b
# Example: using birthday month and day
side_a = 5      # Birthday month example: May
side_b = 15     # Birthday day example: 15

area = side_a * side_b

print("Side A is " + str(side_a))
print("Side B is " + str(side_b))
print("The area of the rectangle is " + str(area))


# ============================================================
# File: tip_amount.py
# Location: week-05/Ex2A_MathScripts/tip_amount.py
# ============================================================

# Formula: tip amount = restaurant bill * tip percentage
restaurant_bill = 50.00
tip_percentage = 0.20

tip_amount = restaurant_bill * tip_percentage

print("The tip on a $" + format(restaurant_bill, ".2f") + " restaurant bill is $" + format(tip_amount, ".2f"))


# ============================================================
# File: area_of_circle.py
# Location: week-05/Ex2A_MathScripts/area_of_circle.py
# ============================================================

# Formula: area = pi * radius * radius
# The radius is half of the diameter.
pi = 3.14159
diameter = 15      # Example birthday day
radius = diameter / 2

circle_area = pi * radius * radius

print("The area of a circle with radius " + str(radius) + " is " + format(circle_area, ".2f"))


# ============================================================
# File: rule_of_72.py
# Location: week-05/Ex2A_MathScripts/rule_of_72.py
# ============================================================

# Rule of 72 formula:
# years to double = 72 / interest rate
current_savings = 1000.00
interest_rate = 0.06

doubled_balance = current_savings * 2
years_to_double = 72 / (interest_rate * 100)

print("Your current savings is " + format(current_savings, ".2f") + ".")
print(
    "At a " + format(interest_rate, ".0%") +
    " interest rate, your savings account will be worth " +
    format(doubled_balance, ".2f") +
    " in " + format(years_to_double, ".1f") + " years"
)


# ============================================================
# Lab 3 Example: input() version
# You can save this as:
# week-05/Ex2A_MathScripts/tip_amount_input.py
# ============================================================

# input() always gives the value as text/string.
# We use float() to convert the input into a decimal number so Python can calculate with it.
# Possible pitfall: if the user types words instead of numbers, the program will give an error.

bill_input = float(input("What is the restaurant bill amount? "))
tip_percent_input = float(input("What tip percentage do you want to leave? Example: enter 20 for 20% "))

tip_percent_decimal = tip_percent_input / 100
tip_amount_input = bill_input * tip_percent_decimal

print("The tip on a $" + format(bill_input, ".2f") + " restaurant bill is $" + format(tip_amount_input, ".2f"))


# ============================================================
# Lab 4 Example: f-string version
# You can save this as:
# week-05/Ex2A_MathScripts/f_string_example.py
# ============================================================

food_cost = 79.25
tax = 6.54
tip = 12.00

total_due = food_cost + tax + tip

# f-strings let us place variables directly inside curly braces.
print(f"Food cost is {food_cost} and tax is {tax}")
print(f"Tip is {tip:.2f}")
print(f"Total due is {total_due:.2f}")