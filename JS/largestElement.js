/**
 * Finds the largest element in an array of numbers.
 *
 * @param {number[]} arr - The array of numbers to search.
 * @returns {number} The largest element in the array.
 */
function findLargestElement(arr) {
    let largest = arr[0];
    for (let i = 1; i < arr.length; i++) {
        if (arr[i] > largest) {
            largest = arr[i];
        }
    }
    return largest;
}

const numbers = [8, 2, 11, 5, 9, 3];
console.log(`The largest element in the array is: ${findLargestElement(numbers)}`);
