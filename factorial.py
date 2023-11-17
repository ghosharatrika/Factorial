# To calculate the factorial using recursion function and to print the time taken to perform it

import timeit


def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


# Input from the user
num = int(input("Enter a non-negative integer: "))

# Check if the input is non-negative
if num < 0:
    print("Please enter a non-negative integer.")
else:
    # Measure the time taken

    start_time = timeit.default_timer()  # To get the time at which the calculation has started
    fact = factorial(num)
    elapsed_time = timeit.default_timer() - start_time  # To get how much time is taken to perform the task

    print(f"The factorial of {num} is {fact}")
    print(f"Time taken: {elapsed_time} seconds")
