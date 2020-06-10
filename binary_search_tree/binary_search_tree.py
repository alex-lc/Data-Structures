"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if the root node is equal to the target, return True
        if self.value == target:
            return True
        # do we have a child node to the left?
        if self.left != None:
            # if the root is bigger than the target, we must be on the left
            if self.value > target:
                if self.left == target:
                    return True
                else:  # recursion, keep checking if the left equals the target
                    return self.left.contains(target)
        # do we have a child node to the right?
        if self.right != None:
            # if the root is smaller than the target, we must be on the right
            if self.value < target:
                if self.right == target:
                    return True
                else:  # recursion, keep checking if the right equals the target
                    return self.right.contains(target)
        else:
            return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.value != None:
            max = self.value
            if self.right != None:
                max = self.right
                return self.right.get_max()
            return max
        else:
            return None

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        pass

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
