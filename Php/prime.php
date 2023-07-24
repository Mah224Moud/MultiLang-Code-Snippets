<?php

/**
 * Checks if a given number is prime.
 *
 * @param int $number The number to check.
 * @return bool Returns true if the number is prime, false otherwise.
 */
function is_prime(int $number): bool
{
    if ($number <= 1) {
        return false;
    }

    $number_sqrt = sqrt($number);
    for ($i = 2; $i <= $number_sqrt; $i++) {
        if (($number % $i) == 0) {
            return false;
        }
    }
    return true;
}

echo is_prime(-1) . PHP_EOL;
echo is_prime(3) . PHP_EOL;
echo is_prime(13578) . PHP_EOL;
echo is_prime(999983) . PHP_EOL;