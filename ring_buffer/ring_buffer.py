from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        
        if self.storage.length < self.capacity:
            #add item to the tail
            self.storage.add_to_tail(item)
            return
        #if current has no value
        if self.current == None:
            self.current = self.storage.head
        #sets the current value to the item
        self.current.value = item
        #add the next value
        self.current = self.current.next
    

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        curr = self.storage.head

        #while there is a current:
        while curr:
            #adds 
            list_buffer_contents.append(curr.value)
            curr = curr.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
