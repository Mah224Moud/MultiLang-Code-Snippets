#include <stdio.h>

/**
 * Calculate the mean value of an array of doubles.
 *
 * @param arr (double[]): The array of doubles.
 * @param length (int): The length of the array.
 *
 * @return (double): The mean value of the array.
 */

double arrayMean(double arr[], int length);

/**
 * Find the minimum value in an array of doubles.
 *
 * @param arr (double[]): The array of doubles.
 * @param length (int): The length of the array.
 *
 * @return (double): The minimum value in the array.
 */

double arrayMin(double arr[], int length);

/**
 * Find the maximum value in an array of doubles.
 *
 * @param arr (double[]): The array of doubles.
 * @param length (int): The length of the array.
 *
 * @return (double): The maximum value in the array.
 */
double arrayMax(double arr[], int length);

int main()
{
    double values[] = {-10.0, 35.0, 12.5, 5.0, 8.0, 11.5};
    int length = sizeof(values) / sizeof(values[0]);

    double mean = arrayMean(values, length);
    double min = arrayMin(values, length);
    double max = arrayMax(values, length);

    printf("The mean is: %.2f\n", mean);
    printf("The min is: %.2f\n", min);
    printf("The max is: %.2f\n", max);

    return 0;
}

double arrayMean(double arr[], int length)
{
    double sum = 0;
    for (int i = 0; i < length; i++)
    {
        sum += arr[i];
    }
    return sum / length;
}

double arrayMin(double arr[], int length)
{
    double min = 0;
    for (int i = 0; i < length; i++)
    {
        if (i == 0)
        {
            min = arr[i];
        }
        else
        {
            if (arr[i] < min)
            {
                min = arr[i];
            }
        }
    }
    return min;
}

double arrayMax(double arr[], int length)
{
    double max = 0;
    for (int i = 0; i < length; i++)
    {
        if (i == 0)
        {
            max = arr[i];
        }
        else
        {
            if (arr[i] > max)
            {
                max = arr[i];
            }
        }
    }
    return max;
}