#include <iostream>
using namespace std;

/**
 * Function to input a positive value from the user.
 *
 * @return int The positive value entered by the user.
 */
int inputPositiveValue()
{
  int value;
  do
  {
    cout << "Enter a strictly positive value:" << endl;
    cin >> value;
  } while (value < 0);
  return value;
}

/**
 * Calculate the sum and product of the first n even numbers.
 *
 * @param n The number of even numbers to consider.
 * @param sum Reference to store the sum of even numbers.
 * @param product Reference to store the product of even numbers.
 */
void calculateSumAndProductOfEvenNumbers(int n, int &sum, int &product)
{
  sum = 0;
  product = 1;

  for (int i = 1; i <= (2 * n); ++i)
  {
    if ((i % 2) == 0)
    {
      sum += i;
      product *= i;
    }
  }
}

/**
 * Main program that uses the above functions.
 *
 * Prompts the user for a value, calculates the sum and product
 * of the first n even numbers, and displays the results.
 */
int main()
{
  int value, sum, product;

  value = inputPositiveValue();

  calculateSumAndProductOfEvenNumbers(value, sum, product);

  cout << "The sum is: " << sum << endl;
  cout << "The product is: " << product << endl;
  return 0;
}
