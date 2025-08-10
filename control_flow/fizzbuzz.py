# **FizzBuzz with Assignment Expression**  
# Write a function `fizzbuzz(n)` that prints numbers 1…n, substituting “Fizz”, “Buzz”, 
# or “FizzBuzz” using a single `for` loop.

def fizzbuzz(n):
    for i in range(1,n+1):
        if(i % 3 == 0 and i % 5 == 0):
            print("FizzBuzz")
        elif(i % 3 == 0):
            print("Fizz")
        elif(i%5 == 0):
            print("Buzz")
        else:
            print(i)

fizzbuzz(15)
