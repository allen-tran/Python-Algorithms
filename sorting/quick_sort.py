"""
Time Complexity: O(n log n)
"""


def quick_sort(sequence):

    length = len(sequence)  # declare length
    if length <= 1:  # when sequence is empty we can just return the empty sequence
        return sequence
    else:  # if not, lets take the last number in the list and store it as a pivot
        pivot = sequence.pop(0)

    items_greater = []  # create greater than list
    items_lower = []  # create less than list

    for item in sequence:  # loop through the items in the list
        if (
            item > pivot
        ):  # if the item is greater than the pivot, append it to the items greater list
            items_greater.append(item)
        else:  # else append it to the items less list
            items_lower.append(item)

    # concatanate the less than and the greater than list with the pivot
    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)


print(quick_sort([3, 5, 7, 4, 2, 4, 6, 4, 5, 6, 4]))  # random input
