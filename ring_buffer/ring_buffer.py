from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # if storage length is less than buffer capacity
        if self.storage.length < self.capacity:
            # add to tail
            self.storage.add_to_tail(item)
            # set current node to tail
            self.current = self.storage.tail
            # if after adding to tail, buffer has reached capacity
            if self.storage.length == self.capacity:
                # form a ring, by setting the current node's next to head
                self.current.next = self.storage.head
                # then remind us that we are doing well
                print("Ooin! You are doing well!!")
        else:
            # otherwise, replace the current node's next value with the item (keeping the formed loop)
            self.current.next.value = item
            # then move current node's pointer to its next
            self.current = self.current.next

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        # start from the head
        current = self.storage.head
        # initilize a counter
        iter_count = 0
        # while counter is less than capacity
        while iter_count < self.capacity:
            # if node exists
            if current is not None:
                # place it's value in the list
                list_buffer_contents.append(current.value)
                # then move current node's pointer to its next
                current = current.next
            # Increment counter
            iter_count += 1

        return list_buffer_contents


# buffer = RingBuffer(3)
# buffer.append('a')
# buffer.append('b')
# buffer.append('c')
# print(buffer.get())
# buffer.append('d')
# buffer.append('e')
# buffer.append('f')
# print(buffer.get())
# buffer.append('g')
# buffer.append('h')
# buffer.append('i')
# print(buffer.get())

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        # this line overrides the element at the given index
        self.storage[self.current % self.capacity] = item
        # increment current
        self.current += 1

    def get(self):
        # use filter to remove None values in case the
        return list(filter(None, self.storage))
