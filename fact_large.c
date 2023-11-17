// This program calculate the factorial of large number

#include <stdio.h>
#include <time.h>
 
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
 
    printf("Factorial of given number is \n");
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
 
int main()
{
    int num;

    printf("Enter a positive number: ");
    scanf("%d",&num);

    clock_t start_time = clock();
    factorial(num);
    clock_t end_time = clock();
    // Calculate elapsed time in seconds
    double elapsed_time = ((double)(end_time - start_time)) / CLOCKS_PER_SEC;
    printf("\nTime taken: %f seconds\n", elapsed_time);
    return 0;
}
