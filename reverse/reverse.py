class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        # reference to the head of the list
        self.head = None

    def add_to_head(self, value):
        node = Node(value)
        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False
        # get a reference to the node we're currently at; update this as we traverse the list
        current = self.head
        # check to see if we're at a valid node
        while current:
            # return True if the current value we're looking at matches our target value
            if current.get_value() == value:
                return True
            # update our current node to the current node's next node
            current = current.get_next()
        # if we've gotten here, then the target node isn't in our list
        return False

    def reverse_list(self):
        # initialize current node from head
        current_node = self.head
        # while current node is not None
        while current_node:
            self.add_to_head(current_node.value)
            current_node = current_node.next_node

    def reverse_list1(self):
        # TO BE COMPLETED
        # initialize current node from head
        current_node = self.head
        # initialize a variable to hold previous node
        prev_node = None
        # while current node is not None
        while current_node:
            # initialize a variable to hold the next node
            next_node = current_node.next_node
            # set previous as new next
            current_node.set_next(prev_node)
            # current_node becomes previous, advancing right
            prev_node = current_node
            # current_node becomes next_node,
            current_node = next_node
            # head becomes prev_node
            self.head = prev_node

    def recursive_reverse_helper(self, curr, prev):
        # If last node. set as head
        if curr.next_node is None:
            self.head = curr
            # set next to prev node
            curr.next_node = prev
            return
        # initialize a variable to hold the next node
        next = curr.next_node
        # set previous as new next
        curr.next_node = prev
        # recursively call the function on next and curr
        self.recursive_reverse_helper(next, curr)

    def recursive_everse_list(self):
        # base case: empty list
        if self.head is None:
            return
        # call helper function
        self.recursive_reverse_helper(self.head, None)
