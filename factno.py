"""
This program  calls the function factorial() from C program file "factorial.c"
"""

from ctypes import *
factlib = CDLL("./factorial.so")

n = int(input("Enter a positive no.:"))
fact = factlib.factorial(n)
print("Factorial of the number", n," : ",fact)

"""
C code for finding factorial of n
-------------------------------------------------------------------------------------------

#include<stdio.h>

long int factorial(int n) // Function to calculate factorial
{
    if (n<=1){
        return 1;
    }
    else{
        return n*factorial(n-1);
    }
}
"""

