# GLOBAL VARIABLES
num1 = 0
num2 = 0
sum = 0
difference = 0

# INPUTS
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# CODE FUNCTIONS
def calculate_sum ():
    global sum, num1, num2
    sum = num1 + num2

def calculate_difference ():
    global difference, num1, num2
    difference = num1 - num2

calculate_sum()
calculate_difference()

print ("Sum :", sum)
print ("Difference :", difference)

