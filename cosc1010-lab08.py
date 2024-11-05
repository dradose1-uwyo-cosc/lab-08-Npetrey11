# Nikita Petrey
# UWYO COSC 1010
# 11/04/2024
# Lab 16
# Lab Section: 16
# Sources, people worked with, help given to:


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 

def adv_convert(num):
    negative = False
    if num[0] == "-":
        negative = True
        num = num.replace("-", "")
    
    if "." in num:
        numsplit = num.split(".") # [somenumber, somenumber]
        if len(numsplit) == 2 and numsplit[0].isdigit() and numsplit[1].isdigit():
            if negative:
                return -1*float(num)
            else:
                return float(num)
        else:
            return False
    elif num.isdigit():
        if negative:
            return -1*int(num)
        else:
            return int(num)
    
    return False

print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list
 
def slope_intercept(m, b, lower_bound_x, upper_bound_x):
    y = []
    if type(lower_bound_x) is int and type(upper_bound_x) is int and lower_bound_x <= upper_bound_x:
        for x in range(lower_bound_x, upper_bound_x):
            y.append((m*x)+b)
    else:
        return False
    return y

while True:
    m = input("Enter value for m(Enter exit to end inputs):")
    if m == 'exit':
        break
    b = input("Enter value for b:")
    lower_bound_x = input("Enter value for lower bound of x:")
    upper_bound_x = input("Enter Value for upper bound of x:")
    m = adv_convert(m)
    b = adv_convert(b)
    lower_bound_x = adv_convert(lower_bound_x)
    upper_bound_x = adv_convert(upper_bound_x)
    y = slope_intercept(m, b, lower_bound_x, upper_bound_x)
    print(y)

print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null
