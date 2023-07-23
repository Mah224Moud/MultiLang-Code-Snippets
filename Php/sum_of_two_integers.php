<?php


/**
 * Calculates the sum of two integers.
 *
 * This function takes two integer arguments and returns their sum.
 *
 * @param int $first_number The first integer.
 * @param int $second_number The second integer.
 * @return int The sum of the two integers.
 */
function sum_of_two_integers(int $first_number, int $second_number): int
{
    return $first_number + $second_number;
}

// Example usage:
echo sum_of_two_integers(12, 13);
