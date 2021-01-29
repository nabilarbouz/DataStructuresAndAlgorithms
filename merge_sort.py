"""
Nabil Arbouz
Algorithms Spring 2020
HW 2
Merge Sort
"""
import random


def merge_sort(lst):
    """
    This is a merge sort function that utilizes recursion
    :param lst: the list(array) we want to sort
    :return: None
    """
    # Initial check for list length greater than 1
    if len(lst) > 1:
        # Split the list into two half-sized lists
        mid = len(lst) // 2
        left_list = lst[:mid]
        right_list = lst[mid:]
        # recursively call the function again to keep splitting the list up
        merge_sort(left_list)
        merge_sort(right_list)

        # this section merges the lists back together by appending the bottom
        # the smallest values in each of the lists
        left_list_counter = 0
        right_list_counter = 0
        sorted_list_counter = 0

        while left_list_counter < len(left_list) \
                and right_list_counter < len(right_list):
            if left_list[left_list_counter] < right_list[right_list_counter]:
                lst[sorted_list_counter] = left_list[left_list_counter]
                left_list_counter += 1
                sorted_list_counter += 1
            else:
                lst[sorted_list_counter] = right_list[right_list_counter]
                right_list_counter += 1
                sorted_list_counter += 1
        # If we didnt go completely through either of the lists, we append
        # the remaining values
        while left_list_counter < len(left_list):
            lst[sorted_list_counter] = left_list[left_list_counter]
            left_list_counter += 1
            sorted_list_counter += 1

        while right_list_counter < len(right_list):
            lst[sorted_list_counter] = right_list[right_list_counter]
            right_list_counter += 1
            sorted_list_counter += 1


def main():
    # initialize an empty list(array)
    lst = []

    # populate the list(array) with random integers
    for x in range(50):
        lst.append(random.randint(-100, 100))
    test_list = lst.copy()

    # Test Cases
    # lst2 = [0, 0, 0, 0]
    # lst2 = []
    # lst2 = [5, 6, 8, 12, 54]
    # lst2 = [1]
    # lst2 = [5, 3, 47, 34, 4]
    # lst2 = [19, 15, 7, 4, 3]

    # Print the before and after of the sort
    print(lst)
    merge_sort(lst)
    print(lst)
    # test_list.sort()
    # print(test_list)
    # print(lst2)
    # merge_sort(lst2)
    # print(lst2)


main()
