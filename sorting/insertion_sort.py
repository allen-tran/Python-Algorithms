'''
Time Complexity: O(n^2) (two nested lists)
Sorted and Unsorted Sub-list
'''

def insertion_sort(list_a):
    indexing_length = range(1, len(list_a))
    for i in indexing_length:
        value_to_sort = list_a[i]

        while list_a[i-1] > value_to_sort and i > 0:
            list_a[i], list_a[i-1] = list_a[i-1], list_a[i]
            i = i -1
    return list_a

print(insertion_sort([7,4, 3,56,67, 4,3,5, 7,3,232, 5,53,2, 32, 435]))