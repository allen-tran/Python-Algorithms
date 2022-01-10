"""
https://leetcode.com/problems/flipping-an-image/
"""


def flip(image):
    # list of lists, we will store the new image
    doublelist = []
    # for the lists in the image
    for i in image:
        # create temp varaible to get the lists in reverse
        newList = i[::-1]
        # append the list to the double list
        doublelist.append(newList)
    # for the list in double list
    for i in doublelist:
        # for the elements within the list of the list
        for j in range(len(i)):
            # if the element equal to 1, switch it to zero
            if i[j] == 1:
                i[j] = 0
            # else, its zero, so switch it to 1
            else:
                i[j] = 1
    # return the new image
    return doublelist


# test
print(flip([[1, 1, 0], [1, 0, 1], [0, 0, 0]]))
