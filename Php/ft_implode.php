<?php

    /**
     * @brief Joins the elements of an array into a single string with a specified separator.
     * 
     * Combines all the elements of an array into a single string, using the specified separator
     * between each pair of elements. If the array is empty, an empty string is returned.
     * 
     * @param string $separator The delimiter used to separate the array elements.
     * @param array $elements The array of elements to join into a string.
     * @return string The resulting string after joining the array elements with the separator.
     */
    function ft_implode(string $separator, array $elements): string
    {
        $resultString = "";

        if (empty($elements)) {
            return $resultString;
        }

        $resultString .= $elements[0];
        $currentIndex = 1;

        while (isset($elements[$currentIndex])) {
            $resultString .= $separator . $elements[$currentIndex];
            $currentIndex++;
        }

        return $resultString;
    }

    /**
     * 
     * Exemple 
     * ````
     * echo ft_implode("," ,['apple', 'banana', 'cherry']),PHP_EOL; // Output: apple, banana, cherry
     * echo ft_implode(".",[192,168,15,160]); // Output: 192.168.15.160
     */
