
# from typing import Sequence


def binary_search(sequence, item):
    begin_index = 0  # get the indices of beginning and end
    end_index = len(sequence) - 1

    while begin_index <= end_index:  # while there are items in the list
        # we find the middle index with floor division
        midpoint = begin_index + (end_index - begin_index) // 2
        # with the middle index we get the actual value
        midpoint_value = sequence[midpoint]
        if midpoint_value == item:  # if the middle value is what we are looking for, return the midpoint
            return midpoint
        elif item < midpoint_value:  # else if the item is less than the midpoint value
            end_index = midpoint - 1  # the end index becomes the first half last value
        else:
            # else the beginning index becomes the seconmd half start value
            begin_index = midpoint + 1
    return None


sequence = [11]
item = 11

print(binary_search(sequence, item))
