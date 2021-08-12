'''
Time Complexity: O(n^2)
'''

def bubble_sort(sequence):
    index_length = len(sequence) - 1 # define last index

    sorted = False # create sorted flag
    while not sorted: # while its not sorted
        sorted = True # first set sorted to true but if it enters the if statement, its not truly sorted
        for i in range(0, index_length): # for loop going until the last index
            if sequence[i] > sequence[i+1]: # if the current index is greater than the next index
                sorted = False # it is not sorted
                sequence[i], sequence[i+1] = sequence[i+1], sequence[i] # swap the values

    return sequence # sequence should be sorted

print(bubble_sort([4,6,3,2,6,7,8,5,3,6,8])) # random list of numbers for testing
