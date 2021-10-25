'''
Time Complexity: O(n^2) (two nested lists)
Sorted and Unsorted Sub-list
'''


def insertion_sort(list_a):
    # getting the range from 1-16
    indexing_length = range(1, len(list_a))

    # for the numbers within the list
    for i in indexing_length:
        # we are going to look at each value to compare it
        value_to_sort = list_a[i]

        # while the number before the val we are looking at is less than the value to sort,
        while list_a[i-1] > value_to_sort and i > 0:
            # we can just swap the two numbers
            list_a[i], list_a[i-1] = list_a[i-1], list_a[i]
            # we can go ahead and decrement i to go down the list and check to see if the values are sorted
            i -= 1
    return list_a


print(insertion_sort([7, 4, 3, 56, 67, 4, 3, 5, 7, 3, 232, 5, 53, 2, 32, 435]))
