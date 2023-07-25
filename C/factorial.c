#include <stdio.h>

long int factorial(int number);

int main()
{
    int number = 0;
    printf("Enter a number: ");
    scanf("%d", &number);

    printf("Factorial of %d is %ld\n", number, factorial(number));
    return 0;
}

/**
 * Calculates the factorial of a given number.
 * @param number The number for which to calculate the factorial.
 * @return The factorial of the given number.
 */
long int factorial(int number)
{

    if (number == 1 || number == 0)
    {
        return 1;
    }
    else
    {
        return number * factorial(number - 1);
    }
}
