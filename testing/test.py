	# binary search O(log2n)
	# mid = 0
	# start, end = 0, len(end)-1

	# if the target less than the midpoint
		# set end to be midpoint
			# then split again
	# elif target greater than midpoint
		# set the start to be midpoint
			# split again
	# else return mid
def find(arr, target):
    # mid = None

    def help(start, end):
        
        mid = (end-start) // 2
        if target == arr[mid]:
            return mid
        if start == end:
            return -1
        if target < arr[mid]:
            #update end
            end = mid
            help(start, end)
        elif target > arr[mid]:
            start = mid
            help(start, end)
        

    return help(0, len(arr)-1)
find([1,2, 3, 4, 5], 4)