
# Calculating Euler's constant

This is a project based on a new function to calculate euler's constant with a time efficiency of 160% compared to the original function :

- (1 + 1/x)^x
or ![](https://raw.githubusercontent.com/TJulesL/euler/main/img/image.png)


The goal of this project is to optimize and perfect the new function. For the new function and other details please read the explanation.


## Explanation

So we will start to take a deep dive into 
```
1. What is euler's constant
2. How do you calculate it normally
3. The new function (Explanation)
4. Running Tests
5. Conclusion
```

### What is euler's constant
Euler's number, often referred to as (e), is a fundamental mathematical constant approximately equal to 2.71828... It is significant because it serves as the base of the natural logarithm and plays a crucial role in various mathematical concepts, including exponential growth and decay models, calculus, and financial calculations such as compound interest. 

Unlike other mathematical constants like pi, (e) is both irrational (meaning it cannot be expressed as a simple fraction) and transcendental (not a root of any non-zero polynomial equation with integer coefficients) Its unique properties make it indispensable in numerous fields of science and engineering. The derivative of e^x is also e^x which is very special.

### How do you calculate it normally

There are a few different ways to calculate euler. However one of the most implemented ways in code is this : 

- f(x) = (1 + 1/x)^x

![](https://raw.githubusercontent.com/TJulesL/euler/main/img/image.png) = e

What this means is that the closer x gets to positive infinity the closer the output of the function gets to euler's number (e).


### The new function (Explanation)

The new function is noted like this : 

((1 + 1/x)^x + (1 + 1/-x)^-x) / 2


Now lets go back and see why this would work / where it would come from. If you look at the normal function in a graph you will see this : 

![](https://raw.githubusercontent.com/TJulesL/euler/main/img/image2.png)


I have drawn the number e as the blue line so you can see that when the number gets bigger it becomes closer and closer to eulers number. You can also see that it will aproach eulers number from a lower value and will never become higher than (e) only more precise.

If you look to the left of the graphical representation you will see a line coming down again (logical because of 1/x) but if you look closely it also aproaches euler but from a higher value. It will close in to eulers number and get more accurate but will never be smaller than (e). Simply said : 

- x < e
- -x > e
- lim x → ∞ = e
- lim -x → -∞ = e


Now you maybe will be able to see what the new function does. It takes both -x and x and calculates them. -x will be larger than e and x smaller. So what it does is add them together and divide by 2 to get the average. Since both values are "as far away" from euler as eachother the average will be very close to euler. Ofcourse just like when you take the average of 2.6 and 2.8 you wont get 2.7182818... but it will at least be close than 2.6 or 2.8

Its a very simple change but it does seriously affect performance and accuracy. I will show you how much by running some tests 

## Running Tests

I have run some tests to see how efficient it is and if it even works more at all. All the code i use will be provided. 

**Note that i did all these test's in python with the code provided without any optimizations** If you can implement it in other code languages please make an issue or commit and i will add it to the repository


First we want to know if its more accurate and how much more. We do this using the Decimal module in python so that we dont have any fixed floating point size which would make the calculation more inaccurate as it gets bigger. It would also prevent other things like OverflowError's

I will provide the snippet of code here :
```python
from decimal import Decimal, getcontext

# setting the precision. I like to set it 1 higher just to make sure 
getcontext().prec = 601

def original_function(x): 
    return ((1 + 1 / x) ** x)
def new_function(x, y): 
    return (((1 + 1 / x) ** x) + ((1 + 1 / y) ** y)) / 2



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




# From here on it prints everything and also uses the compare_decimals() function to check how accurate they are apart from eachother
# I wont put the function in here because its pretty big but if you want to take a look the code is provided

print(f"{a}\n")
print(f"{b}\n")
print(f"{c}\n")
print(f"original : {original_function_time} \nmy time : {new_function_time}")


print("normal function accuracy:", compare_decimals(a, c))
print("new function accuracy:", compare_decimals(b, c))


print(f"difference = {original_function_time - new_function_time}")
```


Now you may be asking why we use 10^250 and -(10^250) and for the original function we use 10^500. I will explain using the test results. times may vary on depending on how powerful your cpu is but i got this : 

```
# in front of this it will print out the numbers so you can see for yourself

original : 0.10601019859313965
my time : 0.06528234481811523
normal function accuracy: 500
new function accuracy: 500
difference = 0.040727853775024414
```

The reason i changed the numbers to about half the amount of zero's. Note that this is not divided by 2 because then it would be 10^499 and that we used 10^500 as number for original function and that it has 500 correct digits so we can say with high confidence that 10^x = x digits in precision for the original function. 

So we take the root of the original number for the original function and put it in the new function which gets us both the same accuracy. However that would not really explain the time difference of 40% less for the new function. It would also look a bit weird when you see that the new function has a lot more calculations to do.

Personally i think it has to do with the fact that it has to work with much smaller numbers which would be more efficient. Im pretty certain of it but i cant say it for sure. What i do know for sure is every time i execute the function with the parameters i gave in the example it will almost always give me the same test results or very close to them.

Here is a little test when we just use a small number and look at the accuracy when using the same number
```
original_function_number = Decimal(10 ** 10)
new_function_number = Decimal(10 ** 10)
accuracy_check_number = Decimal(10 ** 50)

OUTPUT : 

original : 0.0
my time : 0.0
normal function accuracy: 10
new function accuracy: 20
difference = 0.0

(it doesnt display a time because of the calculation being in less than a milisecond)

```
You can see very clear that our function is twice as accurate. We can now go further to test the efficiency in time when the number gets larger. We will also test how it does with 2^x. Because of binairy numbers being either one or 2 instead of a complicated calculation it just for each power has to move a 1 to the left in the binairy space. Here an example: 

```
00000000 = 0
00000010 = 2
00000100 = 4
00001000 = 8
00010000 = 16
. . . . . . .

This makes 2^x very efficient to calculate
```

If you want to try and see for yourself you can just change the values of the number variables to Decimal(2 ** x) x being the power. Its weird to see but when we do the test with 2^x the efficiency drops by 40%. So it now stays around 120% which still is 1.2 times as fast but very much. I mostly think this is because of the original function being less big and therefore having a easier time handling 2^x. 

When we do the same tests with 3^x we get around the same result of 120%. With 4^x we get around 130%. and 5^x is around 140%. I am pretty sure this is because the function works better with larger numbers and 2^x is smaller than 10^x when using the same x. Note that when using 11^x the program glitches because of the E notation out but since we can the bigger the number the more efficiency we can't say with certainty but as a theory that it will only get more efficient over time.

This sounds pretty logical when you know that the new function only needs the square root amount of zero's that the original function uses which makes the numbers increase less (as such also the computational power needed). Figuring this out would take more testing and also changing up the code a little bit but if you want to submit some ideas you're always free to.

In Theory you can say because it is twice as accurate it can be twice as fast to calculate it using 2 times smaller numbers but thats just a theory

We will for now just leave the x^y part at that and continue with 10^x.




Here we have our efficiency test for 10^x

![](https://raw.githubusercontent.com/TJulesL/euler/main/img/Lm2ocq2.png)


In this graph x = the amount in zero's. So if x = 250 then the calculation done for the orignial function 10^250 and for the new function 10^125 and -(10^125)


If we look at percentages we can see it stays around 160% as the numbers get bigger. This means it is 160% more effective in time (with the same accuracy). This means if we input for example 10^1000 in the original function and 10^500 with -(10^500) in the new function it gives the same accuracy of a 1000 digits precision. But **the new function does it 1.6 times faster** which doesnt sound like a lot but when you do a big calculation that takes 10 seconds for the new function it will take 16 for the original function, same with 100 seconds it will take 160 seconds for the original function which is already a whole minute longer. 


#

Now we have explored most of the testing however as you are maybe able to see that mostly in the beginning of all calculations the time really is unstable. Personally i dont really would know why this is. It could have something to do with background programs running but most likely not. It could also be 

Optimization and caching: Modern cpu's and programming languages often optimize arithmetic operations for larger numbers. For instance, python's built-in pow() function might use different algorithms depending on the size of the inputs, optimizing for performance and accuracy with larger numbers

Floating-Point Precision can't really be a problem because of the Decimal import that automatically should fix that problem. However it could also still be Memory Management. Larger numbers require more memory to store and process. When dealing with smaller numbers, the overhead of memory allocation and garbage collection can become a significant factor affecting performance. 

If you know what it is please dont hesitate to make an issue in issues. Thats is mostly all the computation explained if you have any other ideas dont hesitate to bring them up.




## Conclusion

### The new function is 1.6 times faster in time to calculate the same amount of precision (correct Decimals) when using 10^x. When using 2^x the efficiency drops down to only 1.2 times faster than the original most likely caused by the new function being faster in calculating with larger numbers because it only needs the square root of that number to get the same accuracy. 


## Contributing

Contributions or comments / commits / issues are very welcome!

Please adhere to this project's `code of conduct`.


## Authors

- [@TJulesL](https://github.com/TJulesL)


## License

[GPL-3.0](https://choosealicense.com/licenses/gpl-3.0/)

