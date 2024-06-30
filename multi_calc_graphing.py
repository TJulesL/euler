
# Imports the needed libs
import time
from decimal import Decimal, getcontext
import matplotlib.pyplot as plt
import os
import tracemalloc
import numpy
import gc 


# TODO write lists to a json or h5py file to save on memory 
# TODO add support for gpu or / and multiprocessing
# TODO find a better way to measure time / more precise


# Sets Decimal precision to 100
# You can set it to 1 because it adds precision every iteration but i used 100 so it doesnt have the chance to lose any accuracy or give errors
getcontext().prec = 100


# Defining the compare decimals function
def compare_decimals(num1, num2):
    """
    Compares two floating-point numbers and returns the number of matching decimal places.

    :param num1: The first floating-point number.
    :param num2: The second floating-point number.
    :return: The number of matching decimal places.
    """
    # Convert the floats to strings
    str_num1 = str(num1)
    str_num2 = str(num2)

    # Find the decimal point position in each string
    decimal_point1 = str_num1.find('.')
    decimal_point2 = str_num2.find('.')

    # Ensure both numbers have a decimal point
    if decimal_point1 == -1 or decimal_point2 == -1:
        return 0

    # Start comparing from the decimal point
    matching_digits = 0
    for i in range(min(len(str_num1) - decimal_point1 - 1, len(str_num2) - decimal_point2 - 1)):
        # Compare the current digits
        if str_num1[decimal_point1 + i] == str_num2[decimal_point2 + i]:
            matching_digits += 1
        else:
            break
    # Cleaning up vars for memory
    del str_num1, str_num2, decimal_point1, decimal_point2
    return matching_digits




# Defining both of the original and the new function
def original_function(x): 
    return ((1 + 1 / x) ** x)
def new_function(x, y): 
    return (((1 + 1 / x) ** x) + ((1 + 1 / y) ** y)) / 2


# Creating 2 lists to save data for the graph
listdifference = []
list_iterations = []

# Starts the loop with user being able to quit and not quitting the full program
def main():
    try:
        # Set i to the max amount of accuracy you want to have
        for i in range(2000):
            
            # adds precision
            getcontext().prec = i + 1

            # Set's all variables for current iteration
            original_function_num = 10 ** Decimal(i)
            new_function_num = Decimal(10 ** round(i / 2))
            new_function_num_minus = -1 * new_function_num

            if original_function_num == 0.0:
                new_function_num = Decimal(1)
                original_function_num = Decimal(1)
                

            # Takes the time of the new function
            start_my_function = time.time()
            new_function(new_function_num, new_function_num_minus)
            stop_my_function = time.time()
            finish1 = stop_my_function - start_my_function
            
            # Takes the time of the original function
            start_my_function = time.time()
            original_function(original_function_num)
            stop_my_function = time.time()
            finish2 = stop_my_function - start_my_function
            
            # If the time is less than a milisecond skip this iteration
            if finish1 == 0.0:
                continue
            if finish2 == 0.0:
                continue
                
            
            # Calculates the difference
            difference = (finish2 / finish1) * 100
            


            # If no huge spikes just add it to the list
            if difference <= 300.0:
                listdifference.append(difference)
                list_iterations.append(i)
            # if there is a huge spike just set 100% for the current iteration
            if difference >= 300.0:
                listdifference.append(100)
                list_iterations.append(i)
                
            

            
            # Clears and print's isnt really needed but for output
            if i % 10 == 0:
                if i % 100 == 0:
                    # Garbage collection
                    gc.collect()
                os.system("cls")
                print(f"new function: {new_function_num} {finish1}")
                print(f"normal function: {original_function_num}  {finish2}")
                print(f"a difference of {difference} percentage between the values {finish2} and {finish1} ")
            
            # Cleans up iteration and vars for memory
            del difference, new_function_num, finish1, finish2, original_function_num, start_my_function, stop_my_function



    except KeyboardInterrupt:
        pass

# Main function
main()

# When code is done or KeyboardInterrupt make a graph
fig, axs = plt.subplots(1, 1, figsize=(10,10)) # supports more than 1 graph if needed for later development 

# Set iterations as x and difference as y
axs.plot(list_iterations, listdifference, label="difference in percentage")
axs.set_xlabel('iterations and amount')
axs.set_ylabel('percentage')
axs.legend()

# Display the graph
plt.tight_layout()
plt.show()

# Cleaning up
del list_iterations, listdifference
