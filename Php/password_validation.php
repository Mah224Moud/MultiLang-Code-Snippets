<?php

/**
 * Validates the strength of a password.
 * 
 * - A strong password is one that contains at least 16 characters, one uppercase letter, one lowercase letter, one number and one of those special characters @!-_#%$&
 * - A medium password is one that contains at least 10 characters, one uppercase letter, one lowercase letter and one number
 * - A weak password is one that contains at least 8 characters and doesn't match any of the above requirements
 *
 * @param string $password The password to be validated.
 * @return string The validation result message.
 */
function password_validation(string $password)
{
    if (strlen($password) > 8) {
        $low = "/[a-zA-Z]{8,}/";
        $medium = "/^(?=.*\d)(?=.*[A-Z])(?=.*[a-zA-Z])[a-zA-Z\d]{12,}$/";
        $strong = "/^(?=.*\d)(?=.*[A-Z])(?=.*[a-zA-Z])(?=.*[\@\!\-\_\#\%\\$\&])[a-zA-Z\d\@\!\-\_\#\%\\$\&]{16,}$/";

        if (preg_match($strong, $password)) {
            return "Your password is valid and strong";
        } elseif (preg_match($medium, $password)) {
            return "Your password is valid and medium";
        } else {
            return "Your password is valid and weak";
        }

    }

    return "Your password is not valid !!! A password must contain at least 8 characters :)\n";
}

echo password_validation("test123") . PHP_EOL;
echo password_validation("abdeFGHIJ") . PHP_EOL;
echo password_validation("mEVnqselds78") . PHP_EOL;
echo password_validation("mmsZUmHY78@#%!$&") . PHP_EOL;