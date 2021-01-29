"""
Nabil Arbouz

Quicksort Implementation

Test Cases:
Test Case 1:
Input: 5,3,4,2,6
Output: 2,3,4,5,6
Test Case 2:
Input: -3, 5, 4, 3, -10
Output: -10, -3, 3, 4, 5
Test Case 3:
Input: a, d, e, b, f
Output: a, b, d, e, f
Test Case 4:
Input: 1, 1, 1, 1, 1
Output: 1, 1, 1, 1, 1
Test Case 5:
Input: 5, a, b, 2,6
Output: Error
"""


def quick_sort(lst, first, last):
    """
    This is the quicksort function that calls its recursively until the list
    is sorted
    :param lst: a list that is going to be sorted
    :param first: an int that represents the pivot point in the list
    :param last: am int that represents the index of the last position that
    needs to be sorted
    :return: None
    """
    if first < last:
        split_marker = split_list(lst, first, last)

        quick_sort(lst, split_marker + 1, last)
        quick_sort(lst, first, split_marker - 1)


def split_list(lst, first, last):
    """
    This sort the list based on the quicksort algorithm
    :param lst: a list we are going to sort
    :param first: an int that represents the index of the pivot number
    :param last: an int that represents the index that is last in the
    partition
    :return: returns the split mark which is the right_marker
    """
    right_marker = last
    left_marker = first + 1
    done = False

    while not done:
        # We shift the markers until they are in the correct position for swaps
        while lst[left_marker] < lst[first] and left_marker <= right_marker:
            left_marker += 1
        while lst[right_marker] > lst[first] and left_marker <= right_marker:
            right_marker -= 1

        # Check to see if the list is already sorted
        if left_marker > right_marker:
            done = True
        else:
            # We swap the left and the right markers
            lst[left_marker], lst[right_marker] = \
                lst[right_marker], lst[left_marker]

    # now we need to swap the pivot number with the split mark
    lst[first], lst[right_marker] = lst[right_marker], lst[first]

    return right_marker


def main():
    lst = [55, 62, 13, 52, 64]
    print(lst)
    quick_sort(lst, 0, len(lst) - 1)
    print(lst)


main()
