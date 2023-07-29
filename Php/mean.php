<?php
/**
 * Calculates the mean of an array of numbers.
 *
 * @param array $numbers_list The array of numbers.
 * @return float|null The mean of the numbers, or null if the array is empty or doesn't contain any valid numbers.
 */
function mean(array $numbers_list): ?float
{
    $valid_numbers = array_filter($numbers_list, 'is_numeric');

    if (empty($valid_numbers)) {
        return null;
    }

    return array_sum($valid_numbers) / count($valid_numbers);
}


echo mean([12, 145, 234, 345, 98]) . PHP_EOL;
echo mean([12, 33.6, 234, 'ABC', 98]) . PHP_EOL;
echo mean([]) . PHP_EOL;