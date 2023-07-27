<?php

/**
 * Calculates the duration between a start time and an end time and returns it as a formatted string.
 *
 * @param string $startTime The start time in the format 'H:i'.
 * @param string $endTime The end time in the format 'H:i'.
 * @return string The duration formatted as 'hh:mm'.
 */
function getDuration(string $startTime, string $endTime): string
{
    $startTime = DateTime::createFromFormat('H:i', $startTime);
    $endTime = DateTime::createFromFormat('H:i', $endTime);

    $startTimestamp = $startTime->getTimestamp();
    $endTimestamp = $endTime->getTimestamp();

    $minutes = ($endTimestamp - $startTimestamp) / 60;
    $hours = floor($minutes / 60);
    $remainingMinutes = $minutes % 60;

    return sprintf('%02dh:%02dmin', $hours, $remainingMinutes);
}

echo getDuration('12:00', '13:00') . PHP_EOL;
echo getDuration("08:00", "18:34") . PHP_EOL;