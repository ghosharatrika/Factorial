"""
This program  calls the function factorial() from C program file "largefact.c to calculate the factorial of large no.
It also displays total time taken to complete the task.
"""

from ctypes import *
import timeit


largefactlib = CDLL("./largefact.so")

n = int(input("Enter a large positive no.:"))

start_time = timeit.default_timer()
largefactlib.factorial(n)
elapsed_time = timeit.default_timer() - start_time

print("Time taken to find the factorial:",elapsed_time,)
print("\n Factorial of ",n,":")

"""
// This C program calculate the factorial of large number
----------------------------------------------------------------------------------------

#include <stdio.h>

// Maximum number of digits in output
#define MAX 500

int multiply(int x, int res[], int res_size);


void factorial(int n)  // This function finds factorial of large numbers and prints them
{
    int res[MAX];

    // Initialize result
    res[0] = 1;
    int res_size = 1;

    // Apply simple factorial formula n! = 1 * 2 * 3 * 4...*n
    for (int x = 2; x <= n; x++)
        res_size = multiply(x, res, res_size);

    //printf("Factorial of given number is \n");
    for (int i = res_size - 1; i >= 0; i--)
        printf("%d",res[i]);
}

/* This function multiplies x with the number represented by res[]. 
res_size is size of res[] or number of digits in the number represented by res[]. 
This function returns the new value of res_size*/

int multiply(int x, int res[], int res_size)
{
    int carry = 0; // Initialize carry

    // One by one multiply n with individual digits of res[]
    for (int i = 0; i < res_size; i++) {
        int prod = res[i] * x + carry;

        // Store last digit of 'prod' in res[]
        res[i] = prod % 10;

        // Put rest in carry
        carry = prod / 10;
    }

    // Put carry in res and increase result size
    while (carry) {
        res[res_size] = carry % 10;
        carry = carry / 10;
        res_size++;
    }
    return res_size;
}
"""