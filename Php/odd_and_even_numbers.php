<?php
/**
 * Determines if a number is even.
 *
 * @param int $number The number to check.
 * @return bool Returns true if the number is even, false otherwise.
 */
function even($number): bool
{
    return $number % 2 == 0;
}

/**
 * Generates an array with odd and even numbers.
 *
 * @param array $numbers An array of numbers.
 * @return array An associative array with two keys: "even" and "odd". The "even" key contains an array of even numbers, while the "odd" key contains an array of odd numbers.
 */
function array_odd_and_even_numbers($numbers): array
{
    return array(
        "even" => array_filter($numbers, 'even'),
        "odd" => array_diff($numbers, array_filter($numbers, 'even')),
    );
}


// Example output
var_dump(array_odd_and_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]));