<?php

    // Reusing this function which exists in the repository instead of requiring it.

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
     * @brief Splits a string into an array based on a specified separator.
     * 
     * This function traverses the input string and separates it into substrings 
     * whenever the specified separator character is encountered.
     * 
     * @param string $separator The character used as the delimiter.
     * @param string $str The input string to be split.
     * @return array An array of substrings obtained by splitting the input string.
     */
    function ft_explode(string $separator, string $str): array
    {
        $length = calculateStringLength($str); 
        $currentPart = ""; 
        $result = []; 
        $i = 0; 

        while ($i < $length) {
            if ($str[$i] == $separator) {
                $result[] = $currentPart;
                $currentPart = ""; 
            } else {
                $currentPart .= $str[$i]; 
            }
            $i++;
        }

        if ($currentPart !== "") {
            $result[] = $currentPart;
        }

        return ($result);
    }

    /**
     * 
     * Example 
     * ````
     * $array = ft_explode(".","192.168.1.50");
     * var_dump($array); // Output: array(4) {[0]=>
     *                                         string(3) "192"
     *                                         [1]=>
     *                                         string(3) "168"
     *                                         [2]=>
     *                                         string(1) "1"
     *                                         [3]=>
     *                                         string(2) "50"
     *                                         ]}											  
     */