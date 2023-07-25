#include <stdio.h>
#include <stdlib.h>

int isLeapYear(int year);

void findNextDate(int day, int month, int year);

int isLeapYear(int year) {
    if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0)) {
        return 1; // The year is a leap year
    } else {
        return 0; // The year is not a leap year
    }
}

void findNextDate(int day, int month, int year) {
    int daysInMonth[] = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

    // Check if the year is a leap year and adjust the number of days in February
    if (month == 2 && isLeapYear(year)) {
        daysInMonth[month] = 29;
    }

    // Check the validity of the date
    if (month < 1 || month > 12 || day < 1 || day > daysInMonth[month]) {
        printf("The entered date is not valid.\n");
        return;
    }

    if (day < daysInMonth[month]) {
        day++;
    } else {
        day = 1;
        month++;
        if (month > 12) {
            month = 1;
            year++;
        }
    }

    printf("The next date is: %02d/%02d/%d\n", day, month, year);
}

int main() {
    int day, month, year;

    printf("Enter the date (day month year): ");
    scanf("%d %d %d", &day, &month, &year);

    findNextDate(day, month, year);

    return 0;
}
