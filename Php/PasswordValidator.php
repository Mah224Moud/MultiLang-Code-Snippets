<?php

/**
 * Class PasswordValidator
 *
 * This class validates if a password meets specific requirements.
 */
class PasswordValidator {
    /**
     * Verify if a password meets specific requirements.
     *
     * @param string $password The password to verify.
     * @return bool True if the password meets requirements, false otherwise.
     */
    public function isValidPassword($password) {
        // Check if the password contains at least 8 characters
        if (strlen($password) < 8) {
            return false;
        }

        // Check if the password contains at least one special character
        // Using preg_match to search for any of the specified special characters
        // The slashes at the beginning and end of the pattern are delimiters.
        // They indicate the start and end of the regular expression pattern.
        if (!preg_match('/[!@#$%^&*()\-_=+{};:,<.>]/', $password)) {
            return false;
        }

        // Check if the password contains at least 2 digits
        // Using preg_match_all to count the number of digits in the password
        if (preg_match_all('/\d/', $password) < 2) {
            return false;
        }

        // Check if the password contains at least one uppercase letter
        // Using preg_match to search for an uppercase letter
        if (!preg_match('/[A-Z]/', $password)) {
            return false;
        }

        // Check if the password contains at least one lowercase letter
        // Using preg_match to search for a lowercase letter
        if (!preg_match('/[a-z]/', $password)) {
            return false;
        }

        // All conditions passed, password is valid
        return true;
    }
}

// Usage of the PasswordValidator class
$password = "P@ssw0rd1"; // Example password

$validator = new PasswordValidator();
if ($validator->isValidPassword($password)) {
    echo "Password is valid!";
} else {
    echo "Password does not meet the requirements.";
}
