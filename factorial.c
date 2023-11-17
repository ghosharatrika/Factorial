// To calculate factorial of number n in C

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

int main()
{
    int num;
    printf("Enter a positive number: "); //Inputing a number
    scanf("%d",&num);

    if (num<0){
        printf("Wrong input.");
    }
    else{
         printf("Factorial of %d is: %d",num,factorial(num)); // calculating the factorial and printing it
    }
    
    return 0;

}
