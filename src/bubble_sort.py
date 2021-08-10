'''


'''

def bubble_sort(sequence):
    index_length = len(sequence) - 1

    sorted = False
    while not sorted:
        sorted = True
        for i in range(0, index_length):
            if sequence[i] > sequence[i+1]:
                sorted = False
                sequence[i], sequence[i+1] = sequence[i+1], sequence[i]

    return sequence

print(bubble_sort([4,6,3,2,6,7,8,5,3,6,8]))