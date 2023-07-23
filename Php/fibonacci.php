<?php

/**
 * Generate the Fibonacci sequence up to a given limit.
 *
 * @param int $limit The maximum number of elements in the Fibonacci sequence.
 * @return array The Fibonacci sequence up to the given limit.
 */
function fibo(int $limit)
{
    $list = array(0, 1);

    for ($i = 2; $i <= $limit; $i++) {
        $list[] = $list[$i - 1] + $list[$i - 2];
    }
    return $list;
}


$limit = 10;
var_dump(fibo($limit));