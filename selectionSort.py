"""
Nabil Arbouz and Anna Daccache
Hw 1
Selection Sort
Algorithms Spring 2020
"""
from random import *


def selection_sort(input_array):
    """
    This function implements the selection sort algorithm using 1 array
    @param input_array: an array of integers that needs to be sorted
    """
    # Start looping through the array
    for i in range(len(input_array)):
        # The minimum index will increase by 1 on each pass as we sort the array
        min_index = i
        # This loop will find the minimum value in the array to swap
        for j in range(i + 1, len(input_array)):
            if input_array[j] < input_array[min_index]:
                min_index = j
        input_array[i], input_array[min_index] = \
            input_array[min_index], input_array[i]


def main():
    # We seed the random generator to get the same results each time
    seed(0)
    # We initialize the test array with a 0
    test_array = [0]
    # We randomly generate positive and negative integers to append to the array
    for i in range(99):
        test_array.append(randint(-100, 100))
    # Print the unsorted array
    print(test_array)
    # Print the number of elements in the array
    print(len(test_array))
    # Copy the unsorted array for testing purposes
    original_test_array = test_array.copy()
    # Sort the test_array using our selection sort and original_test_array
    # using the built-in Python sort function
    selection_sort(test_array)
    original_test_array.sort()

    # Use a loop to confirm our results.
    for x in range(len(test_array)):
        if test_array[x] != original_test_array[x]:
            print("They are not equal")
            exit()
    print("They are equal")

    print(original_test_array)
    print(test_array)


main()
