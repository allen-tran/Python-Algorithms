from typing import List

"""

Given a binary search tree, retrieve its edges

 * eg            5
 *          2          8
 *        1   3     6     11            q=   0, 3, 8, 7, 13
 *      0         5   7       13
 *
 *
 * Left edge - [5, 2, 1, 0]
 * Right edge - [5, 8, 11, 13]
 * Bottom edge - [0, 3, 8, 7, 13]
 


 the return value should be [[5, 2, 1, 0], [5, 8, 11, 13], [0, 3, 8, 7, 13]]

"""


class Node:
    def __init__(self, val: int, left:'Node'=None, right:'Node'=None) -> None:
        self.val = val
        self.left = left
        self.right = right



from collections import deque



# O(1)

class LinkedNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next




class Queue():

    def __init__(self) -> None:
        self.head = None 
        self.tail = None
        self.size = 0

    def append(self, val):
        new_node = LinkedNode(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1


    def popleft(self):
        if self.size == 0:
            return
        value = self.head.val
        self.head = self.head.next
        self.size -= 1
        return value
    
    
    def __len__(self):
        return self.size


    


        
def retrieve_tree_edges(root: 'Node') -> List[List[int]]:
    """  Your code goes here  """
    ''''
    tree_levels = [[5], [2, 8], [1,3,6,11], [0,3, 8,7,13]]
    tree_levels[-1] would NOT work
    '''
    res = [] # [[][][]]

    bottom = []
    left = []
    right = []

    q = Queue()
    q.append(root)

    while len(q) != 0:
        temp = []
        # temp_right
        length = q.size
        # print(length)
        for i in range(length):
            # print(q)
            rem = q.popleft()
            if not rem.left and not rem.right:
                # leaf node
                bottom.append(rem.val)
            if rem.left:
                q.append(rem.left)
            if rem.right:
                q.append(rem.right)
            # print(rem.val)
            temp.append(rem.val)
        # print(temp)
        res.append(temp)
    
    bottom.sort()

    for i in res:
        #level
        left.append(i[0])
        right.append(i[-1])
    print(left, right, bottom)
    # return [left, right, bottom]
    ''''
    [5]
    [2, 8]
    [1, 3, 6, 11]
    [0, 8, 7, 13]
    '''
    return [[], [], []]







def main():
    
    # left subtree
    zero = Node(0)
    one = Node(1, zero)
    three = Node(3)
    two = Node(2, one, three)
    
    # right subtree
    eight1 = Node(8)
    seven = Node(7)
    six = Node(6, eight1, seven)
    thirteen = Node(13)
    eleven = Node(11, None, thirteen)
    eight2 = Node(8, six, eleven)
    
    # root
    root = Node(5, two, eight2)
    
    left_edge, right_edge, bottom_edge = retrieve_tree_edges(root)
    
    print('\n\n')
    print(left_edge)
    print(right_edge)
    print(bottom_edge)
    
    if left_edge == [5, 2, 1, 0] and right_edge == [5, 8, 11, 13] and bottom_edge == [0, 3, 8, 7, 13]:
        print('PASS')
    else:
        print('FAIL')
        
        
if __name__ == "__main__":
    main()