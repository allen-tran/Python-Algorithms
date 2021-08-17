
from typing import Sequence


def binary_search(sequence, item):
    begin_index = 0 # get the indices of beginning and end
    end_index = len(sequence) - 1

    while begin_index <= end_index: # while there are items in the list
        midpoint = begin_index + (end_index - begin_index) // 2 # we find the middle index with floor division
        midpoint_value = sequence[midpoint] # with the middle index we get the actual value
        if midpoint_value == item: # if teh middle value is what we are looking for, return the midpoint
            return midpoint
        elif item < midpoint_value: # else if the item is less than the midpoint value
            end_index = midpoint - 1 # the end index becomes the first half last value
        else:
            begin_index = midpoint + 1 # else the beginning index becomes the seconmd half start value
    return None


sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10 , 11]
item = 6

print(binary_search(sequence, item))