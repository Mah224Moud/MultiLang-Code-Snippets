<?php

    /**
     * @brief Calculates the length of a given string.
     * 
     * This function iterates through the string to count the number of characters 
     * until the null-terminator is reached. It does not rely on built-in functions.
     * 
     * @param string $str The input string whose length is to be calculated.
     * @return int The length of the input string.
     */

    function calculateStringLength(string $str): int
    {
        $length = 0; 

        // Iterate through the string until no character is found.
        while (isset($str[$length])) {
            $length++;
        }

        return $length;
    }

    /**
     * Example:
     * ```
     * echo calculateStringLength("Hello"); // Output: 5
     * echo calculateStringLength("Have a good day"); // Output: 15
     * echo calculateStringLength("string"); // Output: 6
     * ```
     */