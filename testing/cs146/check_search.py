from typing import Generic, TypeVar
from collections import deque


T = TypeVar("T")


class BinarySearchTree(Generic[T]):
    def __init__(self) -> None:
        self.size = 0
        self.height = -1
        self.root = None

    def insert(self, value: T) -> bool:
        """
        insert a new value to the binary search tree
        @return: whether the function call changed the tree
        """
        new_node = self.Node(value)

        # if the tree is empty, then the new node will be the root
        if self.root == None:
            self.root = new_node
            self.height = 0

        # else, look for the appropriate location for the new node
        else:
            # if tree is not empty, then we know there's at least 1 node which is root
            # and height is at least 0, which is root's level
            current = self.root
            height = 0

            # perform the BST insert logic
            while True:

                height += 1
                parent = current

                if value > current.data:
                    current = current.right_child

                    if current is None:
                        parent.right_child = new_node
                        parent.left_child = self.Node(float("-inf"))
                        break

                elif value < current.data:

                    current = current.left_child

                    if current is None:
                        parent.left_child = new_node
                        parent.right_child = self.Node(float("inf"))
                        break

                # BST does not allow duplicates
                else:
                    return False

            if height >= self.height:
                self.height = height

        self.size += 1

        return True

    def preorder_traversal(self) -> list[T]:
        """
        Perform a preorder traversal and return the list of
        values of the nodes in the tree in preorder rule
        """
        arr = list()
        self.__preorder_traversal(self.root, arr)
        return arr

    def __preorder_traversal(self, parent: "Node", arr: list[T]) -> None:
        """
        helper function for preorder traversal
        """
        if parent is None:
            return

        # preorder traverse: parent -> left -> right
        if parent.data != float("inf") and parent.data != float("-inf"):
            arr.append(str(parent.data))
        self.__preorder_traversal(parent.left_child, arr)
        self.__preorder_traversal(parent.right_child, arr)

    class Node(Generic[T]):
        def __init__(self, data, left=None, right=None) -> None:
            self.data = data
            self.left_child = left
            self.right_child = right


def main():

    print()
    nodes = input("Enter input: ").replace(",", " ").split()
    bst = BinarySearchTree()

    for num in nodes:
        bst.insert(int(num))

    expected = bst.preorder_traversal()

    result = "Failed" if nodes != expected else "True"

    print("\n", result, "\n")


if __name__ == "__main__":
    main()
