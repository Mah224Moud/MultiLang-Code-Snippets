<?php
/**
 * Convert a binary number to decimal representation.
 *
 * This function takes a binary number as input and returns an integer representing
 * the equivalent decimal value.
 *
 * @param int|string $binary The binary number to be converted to decimal. Can be either an integer or a string.
 * @return int The resulting decimal number.
 */
function binary_to_decimal($binary): int
{
    // Convert the input to a string if it's an integer or split it if it's already a string
    $values = is_int($binary) ? str_split(strval($binary)) : str_split($binary);

    $result = 0;
    $pow_index = count($values) - 1;

    foreach ($values as $value) {
        if ($value == 1) {
            $result += pow(2, $pow_index);
        }
        $pow_index--;
    }
    return $result;
}

echo binary_to_decimal("10110") . PHP_EOL;
echo binary_to_decimal(10100) . PHP_EOL;