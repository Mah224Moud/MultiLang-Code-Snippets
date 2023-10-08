#include <iostream>

// Definition of the Date structure
struct Date {
    int jour;  // Day (between 1 and 31)
    int mois;  // Month (between 1 and 12)
};

// Function to check if a date is valid
bool isValidDate(const Date &date) {
    if (date.mois >= 1 && date.mois <= 12 && date.jour >= 1) {
        if (date.mois == 2) {
            // February has 28 days for this exercise (no leap years)
            return date.jour <= 28;
        } else if (date.mois == 4 || date.mois == 6 || date.mois == 9 || date.mois == 11) {
            // Months with 30 days
            return date.jour <= 30;
        } else {
            // All other months with 31 days
            return date.jour <= 31;
        }
    }
    return false; // Invalid month or day
}

// Procedure to input a Date
void inputDate(Date &date) {
    do {
        std::cout << "Enter the day (1-31): ";
        std::cin >> date.jour;
        std::cout << "Enter the month (1-12): ";
        std::cin >> date.mois;
    } while (!isValidDate(date));
}

// Procedure to display a Date
void displayDate(const Date &date) {
    std::cout << date.jour << "/" << date.mois << std::endl;
}

// Function to calculate the next day
Date lendemain(const Date &date) {
    Date nextDate = date;
    nextDate.jour++;

    if (date.mois == 2) {
        // February has 28 days for this exercise
        if (nextDate.jour > 28) {
            nextDate.jour = 1;
            nextDate.mois++;
        }
    } else if (date.mois == 4 || date.mois == 6 || date.mois == 9 || date.mois == 11) {
        // Months with 30 days
        if (nextDate.jour > 30) {
            nextDate.jour = 1;
            nextDate.mois++;
        }
    } else {
        // All other months with 31 days
        if (nextDate.jour > 31) {
            nextDate.jour = 1;
            nextDate.mois++;
        }
    }

    if (nextDate.mois > 12) {
        nextDate.mois = 1;
    }

    return nextDate;
}

int main() {
    Date uneDate;

    // Input a date
    inputDate(uneDate);

    // Display the input date
    std::cout << "Entered date: ";
    displayDate(uneDate);

    // Calculate and display the next day
    Date nextDay = lendemain(uneDate);
    std::cout << "Next day: ";
    displayDate(nextDay);

    return 0;
}
