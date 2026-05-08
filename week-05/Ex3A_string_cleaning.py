# Description: This script cleans messy string data
# Author: Mohamed Mouatakid

# Original contact records
name_1 = "PRIYA SHARMA"
name_2 = "bob NGUYEN"
name_3 = "LaTonya Williams"

salary_1 = "$82,500"
salary_2 = "$74,000"

# Convert names to lowercase
print("Lowercase names:")
print(name_1.lower())
print(name_2.lower())
print(name_3.lower())

# Convert names to title case
print("\nTitle case names:")
print(name_1.title())
print(name_2.title())
print(name_3.title())

# Remove the dollar sign from salary strings
salary_1_no_dollar = salary_1.replace("$", "")
salary_2_no_dollar = salary_2.replace("$", "")

print("\nSalaries without dollar sign:")
print(salary_1_no_dollar)
print(salary_2_no_dollar)

# Test the data type
print(type(salary_1_no_dollar))
print(type(salary_2_no_dollar))

# These values are still strings.
# To perform math on them, we need to remove the comma and convert them to integers.

# Chain replace() and int() together to create a usable integer
salary_1_integer = int(salary_1.replace("$", "").replace(",", ""))

print("\nSalary 1 as an integer:")
print(salary_1_integer)
print(type(salary_1_integer))