# Description: This script tests various numeric
# conversion techniques
# Author: Mohamed Mouatakid

# Original variables
a = " 101.1 "
b = '55'
c = "402 Stevens"
d = 'Number 5 '

# Print original values and types
print("Original variables:")
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))

print("\nConversion tests:")

# Variable a
# int(a) gives ValueError because "101.1" is a decimal string, not a whole number
# a_int = int(a)  # ValueError
a_float = float(a)  # Works because float() accepts decimal numbers and ignores spaces
a_float_then_int = int(float(a))  # Works: converts to 101.1 first, then 101
a_slice = a[1:6]  # Gets only 101.1 without spaces
a_slice_float = float(a_slice)

print("a_float:", a_float, type(a_float))
print("a_float_then_int:", a_float_then_int, type(a_float_then_int))
print("a_slice:", a_slice, type(a_slice))
print("a_slice_float:", a_slice_float, type(a_slice_float))
print("a stripped:", a.strip())  # Removes leading and trailing spaces

# Variable b
b_int = int(b)  # Works because "55" is a whole number string
b_float = float(b)  # Works and returns 55.0
b_slice = b[0:2]  # Gets "55"
b_slice_int = int(b_slice)

print("b_int:", b_int, type(b_int))
print("b_float:", b_float, type(b_float))
print("b_slice:", b_slice, type(b_slice))
print("b_slice_int:", b_slice_int, type(b_slice_int))

# Variable c
# int(c) gives ValueError because the string contains letters
# c_int = int(c)  # ValueError
# float(c) gives ValueError because the string contains letters
# c_float = float(c)  # ValueError
c_slice = c[0:3]  # Gets only the numeric part: "402"
c_slice_int = int(c_slice)

print("c_slice:", c_slice, type(c_slice))
print("c_slice_int:", c_slice_int, type(c_slice_int))

# Variable d
# int(d) gives ValueError because the string contains letters
# d_int = int(d)  # ValueError
# float(d) gives ValueError because the string contains letters
# d_float = float(d)  # ValueError
d_slice = d[7:8]  # Gets only the numeric part: "5"
d_slice_int = int(d_slice)

print("d_slice:", d_slice, type(d_slice))
print("d_slice_int:", d_slice_int, type(d_slice_int))
print("d stripped:", d.strip())  # Removes trailing space