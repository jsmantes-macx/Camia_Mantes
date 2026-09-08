# AUTHOR: Jaz Alexandria S. Mantes
# PURPOSE: Calculate the hypotenuse of a right triangle.

import math

# Ask the user for the lengths of the two shorter sides of the right triangle
a = float(input("Enter the length of the side a: "))
b = float(input("Enter the length of the side b: "))

# Compute the square of the two previously inputted lengths by the user
a_squared = math.pow(a, 2)
b_squared = math.pow(b, 2)

# Compute the sum of the two previously squared lengths
sum_squared = a_squared + b_squared

# Calculate the hypotenuse using the Pythagorean Theorem
c = math.sqrt(sum_squared)

# Display the result of the previously calculated equation with two decimal points
print(f"The distance of the two lengths are: {c:.2f}")