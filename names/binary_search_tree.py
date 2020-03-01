from dll_stack import Stack
from dll_queue import Queue
import sys
sys.path.append('../queue_and_stack')


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # LEFT CASE
        # check if our new nodes value is less than the current nodes value
        if value < self.value:
            # does it have a child to the left?
            if self.left is None:
                # place our new node here
                self.left = BinarySearchTree(value)
            # otherwise
            else:
                # repeat process for the left
                self.left.insert(value)

        # RIGHT CASE
        # check if the new nodes value is greater than or equal to the current nodes value
        if value >= self.value:
            # does it have a child to the right?
            if self.right is None:
                # place our new node here
                self.right = BinarySearchTree(value)
            # otherwise
            else:
                # repeat the process for the right
                self.right.insert(value)
        # return self to allow us chain similar insert operations
        return self

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if the target is the root node, return True
        if self.value == target:
            return True
        # if value is less than root node and left is not None, recurse
        elif target < self.value and self.left:
            return self.left.contains(target)
        # if value is greater than root node and right is not None, recurse
        elif target > self.value and self.right:
            return self.right.contains(target)
        # otherwise
        return False

    # Return the maximum value found in the tree
    def get_max(self):
        # base case: empty tree
        if not self:
            return None
        # maximum value must be on the right
        if not self.right:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # call back on root value
        cb(self.value)
        # if left, traverse and call back
        if self.left:
            self.left.for_each(cb)
        # if right, traverse and call back
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left:
            self.in_order_print(node.left)
        print(node.value)
        if node.right:
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # create an empty queue
        q = Queue()
        # add the starting node to the queue
        q.enqueue(self)

        # iterate over the queue
        while q.len() > 0:
            # set the current_node to the first item in the q
            current_node = q.dequeue()
            # then print the current value
            print(current_node.value)
            # if the current node has a left child
            if current_node.left:
                # call enqueue on the current left
                q.enqueue(current_node.left)
            # if the current node has a right child
            if current_node.right:
                # call enqueue on the current right
                q.enqueue(current_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # create an empty stack
        s = Stack()
        # add the starting node to the stack
        s.push(self)

        # iterate over the stack
        while s.len() > 0:
            # set the current_node to the first item in the stack
            current_node = s.pop()
            # then print the current value
            print(current_node.value)
            # if the current node has a right child
            if current_node.right:
                # call push on the current right
                s.push(current_node.right)
            # if the current node has a left child
            if current_node.left:
                # call push on the current left
                s.push(current_node.left)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
