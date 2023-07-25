#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int split(const char *str, char delimiter, char ***result) {
    int count = 1;
    int len = strlen(str);

    // Count the number of delimiters to determine the size of the array
    for (int i = 0; i < len; i++) {
        if (str[i] == delimiter) {
            count++;
        }
    }

    // Allocate memory for the array of pointers to substrings
    *result = (char **)malloc(count * sizeof(char *));

    if (*result == NULL) {
        fprintf(stderr, "Memory allocation error.\n");
        return 0;
    }

    int index = 0;
    int start = 0;

    // Split the string into substrings based on the delimiter
    for (int i = 0; i <= len; i++) {
        if (str[i] == delimiter || str[i] == '\0') {
            int substringLen = i - start;

            // Allocate memory for each substring
            (*result)[index] = (char *)malloc((substringLen + 1) * sizeof(char));

            if ((*result)[index] == NULL) {
                fprintf(stderr, "Memory allocation error.\n");
                return 0;
            }

            // Copy the substring into the array
            strncpy((*result)[index], &str[start], substringLen);
            (*result)[index][substringLen] = '\0';

            start = i + 1;
            index++;
        }
    }

    return count;
}

int main() {
    const char *str = "Hello,World,Split,Function";
    char delimiter = ',';
    char **result;
    int count = split(str, delimiter, &result);

    if (count > 0) {
        printf("The array contains %d elements:\n", count);
        printf("[");
        for (int i = 0; i < count; i++) {
            if (i == count-1)
                printf("%s", result[i]);
            else
                printf("%s , ", result[i]);
            free(result[i]); // Free the memory allocated for each substring
        }
        printf("]");
        free(result); // Free the memory allocated for the array of pointers
    } else {
        printf("No elements found.\n");
    }
    return 0;
}
