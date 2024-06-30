from decimal import Decimal, getcontext
import time
import gc

# TODO write lists to a json or h5py file to save on memory 
# TODO add support for gpu or / and multiprocessing
# TODO find a better way to measure time / more precise

# Set precision to the highest number needed + 1 (accuracy_check_number + 1)
getcontext().prec = 101
# Define the function to compare decimals
def compare_decimals(num1, num2):
    """
    compares two floats and returns the number of matching decimal places.

    :param num1: the first floating-point number.
    :param num2: the second floating-point number.
    :return: the number of matching decimal places.
    """
    # convert the floats to strings
    str_num1 = str(num1)
    str_num2 = str(num2)

    # find the decimal point position in each string
    decimal_point1 = str_num1.find('.')
    decimal_point2 = str_num2.find('.')

    # ensure both numbers have a decimal point
    if decimal_point1 == -1 or decimal_point2 == -1:
        return 0

    # start comparing from the decimal point
    matching_digits = 0
    for i in range(min(len(str_num1) - decimal_point1 - 1, len(str_num2) - decimal_point2 - 1)):
        # compare the current digits
        if str_num1[decimal_point1 + i] == str_num2[decimal_point2 + i]:
            matching_digits += 1
        else:
            break
    del str_num1, str_num2, decimal_point1, decimal_point2
    return matching_digits



# defining the functions
def original_function(x): 
    return ((1 + 1 / x) ** x)
def new_function(x, y): 
    return (((1 + 1 / x) ** x) + ((1 + 1 / y) ** y)) / 2


# Garbage collection
gc.collect()
# Sets numbers to var's and changes them in to the Decimal module
# 10 ** 10 is the same as 10 with 10 zero's
original_function_number = Decimal(10 ** 500)
new_function_number = Decimal(10 ** 250)
accuracy_check_number = Decimal(10 ** 600)


# uses the original function to check later on how accurate the others are by using a much bigger number
accuracy_check = original_function(accuracy_check_number)


# notes the time it takes for the original function to execute and be done
starttime = time.time()
a = original_function(original_function_number)
stoptime = time.time()

original_function_time = (stoptime - starttime) 



# notes the time for the new function
starttime = time.time()
b = new_function(new_function_number, (-1 * new_function_number))
stoptime = time.time()

new_function_time = (stoptime - starttime) 






# Prints out all 3 calculated e's  
print(f"{a}\n")
print(f"{b}\n")
print(f"{accuracy_check}\n")
# Prints out both the time it took for the original function and the new function
print(f"original : {original_function_time} \nmy time : {new_function_time}")

# Uses the compare_decimals() function to check how accurate they are apart from eachother
print("normal function accuracy:", compare_decimals(a, accuracy_check))
print("new function accuracy:", compare_decimals(b, accuracy_check))

# Prints out difference
print(f"difference = {original_function_time - new_function_time}")

#cleans up
del a, b, accuracy_check, original_function_time, new_function_time, accuracy_check, accuracy_check_number, original_function_number, new_function_number
