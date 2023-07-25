#include <stdio.h>
#include <stdlib.h>

// Binary search function using recursion
int binarySearchRecursive(int arr[], int left, int right, int target) {
    if (left <= right) {
        int mid = left + (right - left) / 2;
        
        if (arr[mid] == target) {
            return mid; // Element found, return the index
        } else if (arr[mid] < target) {
            return binarySearchRecursive(arr, mid + 1, right, target); // Search in the right half
        } else {
            return binarySearchRecursive(arr, left, mid - 1, target); // Search in the left half
        }
    }
    
    return -1; // Element not found, return -1
}

int main() {
    int arr[] = {2, 5, 8, 12, 16, 23, 38, 45, 56, 72, 91};
    int n = sizeof(arr) / sizeof(arr[0]);
    int target = 23;
    
    int result = binarySearchRecursive(arr, 0, n - 1, target); // Call the recursive binary search function
    
    if (result != -1) {
        printf("Element found at index %d\n", result);
    } else {
        printf("Element not found in the array.\n");
    }
    
    return 0;
}
