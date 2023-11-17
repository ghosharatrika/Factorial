#To calculate the factorial from scipy library and print the time taken

from scipy.special import factorial
import timeit

# Input from the user
n = int(input("Enter a non-negative integer: "))

# Check if the input is non-negative
if n < 0:
    print("Please enter a non-negative integer.")
else:
    # Call the factorial function from SciPy
    start_time = timeit.default_timer()  # To get the time at which the calculation has started
    result = factorial(n)
    elapsed_time = timeit.default_timer() - start_time  # To get how much time is taken to perform the task
    print(f"Factorial of ", n, ":", result)
    print(f"Time taken: {elapsed_time} seconds")
