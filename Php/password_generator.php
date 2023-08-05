<?php
/**
 * Generates a random password of the specified length with a random distribution
 * of digits, special characters, and letters (uppercase and lowercase).
 *
 * @param int $length The desired length of the password.
 * @return string The randomly generated password.
 */
function generateRandomPassword(int $length): string {
    $digits = '0123456789';
    $specialChars = '!@#$%^&*()-_=+';
    $letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';

    $numDigits = rand(1, $length - 3); 
    $numSpecialChars = rand(1, $length - 2 - $numDigits);
    $numLetters = $length - $numDigits - $numSpecialChars; 

    $randomDigits = substr(str_shuffle($digits), 0, $numDigits);
    $randomSpecialChars = substr(str_shuffle($specialChars), 0, $numSpecialChars);
    $randomLetters = substr(str_shuffle($letters), 0, $numLetters);

    $password = str_shuffle($randomDigits . $randomSpecialChars . $randomLetters);

    return $password;
}

// Example usage to generate a password of length 15
$generatedPassword = generateRandomPassword(15);
echo $generatedPassword;
