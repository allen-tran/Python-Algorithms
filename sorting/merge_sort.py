'''
Time Complexity: O(n log n)
'''

def merge_sort(sequence):
    if len(sequence) > 1:
        left_arr = sequence[:len(sequence)// 2]
        right_arr = sequence[len(sequence)//2:]

        merge_sort(left_arr)
        merge_sort(right_arr)

        i = 0 # left array index
        j = 0 # right arry index
        k = 0 # new array index

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                sequence[k] = left_arr[i]
                i+=1
            else:
                sequence[k] = right_arr[j]
                j += 1
            k += 1
        while i < len(left_arr):
            sequence[k] = left_arr[i]
            i+=1
            k+=1
        while j < len(right_arr):
            sequence[k] = right_arr[j]
            j+=1
            k+=1


print(merge_sort([1,2,6,2,3,10,8,6,4,6]))