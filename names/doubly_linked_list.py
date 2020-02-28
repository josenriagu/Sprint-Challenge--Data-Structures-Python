"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""

    def add_to_head(self, value):
        # initialize a new node with the given value
        new_node = ListNode(value, None, None)
        # increment length, since we are adding
        self.length += 1
        # edge case: if empty list with no head and tail
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            # link1: let the new_node's next point to the old head
            new_node.next = self.head
            # link2: let the old head's prev point to the new_node
            self.head.prev = new_node
            # reassign the list head to new_node
            self.head = new_node

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):
        # store the value of the head so we can return it
        value = self.head.value
        # delete the head using predefined method
        self.delete(self.head)
        return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        # similar steps to add_to_head
        new_node = ListNode(value, None, None)
        self.length += 1
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            # link new_node and tail
            new_node.prev = self.tail
            self.tail.next = new_node
            # assign new_node as the tail
            self.tail = new_node

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):
        # similar steps to remove_from_head
        value = self.tail.value
        self.delete(self.tail)
        return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):
        # edge case 1: if head, return, since it is already in place
        if node is self.head:
            return
        # get node's value
        value = node.value
        # edge case 2: if tail, remove from tail
        if node is self.tail:
            self.remove_from_tail()
        else:
            # delete the node
            node.delete()
            # decrement the length
            self.length -= 1
        # then add the value to head
        self.add_to_head(value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        # edge case 1: if tail, return, since it is already in place
        if node is self.tail:
            return
        # get node's value
        value = node.value
        # edge case 2: if head, remove from head
        if node is self.head:
            self.remove_from_head()
        else:
            # delete the node
            node.delete()
            # decrement the length
            self.length -= 1
        # then add the value to tail
        self.add_to_tail(value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):
        # decrement the length
        self.length -= 1
        # edge case: if empty list with no head and tail
        if not self.head and not self.tail:
            return
        # edge case: if list has one element which serves as both head and tail
        if self.head == self.tail:
            self.head = None
            self.tail = None
        # edge case: if head is about to be deleted, readjust list head accordingly
        elif self.head == node:
            self.head = node.next
            node.delete()
        # edge case: if tail is about to be deleted, readjust list tail accordingly
        elif self.tail == node:
            self.tail = node.prev
            node.delete()
        else:
            node.delete()

    """Returns the highest value currently in the list"""

    def get_max(self):
        # edge case: if empty list, return None
        if not self.head:
            return None
        # set the max_value to the value of the head
        max_value = self.head.value
        current_node = self.head
        # initialize a loop
        while current_node:
            if current_node.value > max_value:
                max_value = current_node.value
            # assign the current node to its next value, till it gets to tail which has a next of 'None' and the while loop breaks
            current_node = current_node.next
        # return the max_value
        return max_value
