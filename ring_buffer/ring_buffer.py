from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # If the list is empty, add item to the head and the current becomes the head
        if len(self.storage) == 0:
          self.storage.add_to_head(item)
          self.current = self.storage.head
          return

        # If the list is at capacity, remove the oldest (current.next)
        if len(self.storage) == self.capacity:

          # If the current is the tail, overwrite the head
          if self.current == self.storage.tail:
            self.storage.head.value = item
            self.current = self.storage.head

          # Else, if the current.next exists, overwrite the current.next
          else:
            self.current.next.value = item
            self.current = self.current.next

        #Else, if the storage is not at capacity, add value to the tail
        else:
          self.storage.add_to_tail(item)
          self.current = self.storage.tail

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        cursor = self.storage.head

        if cursor == None:
          return list_buffer_contents

        while cursor:
          list_buffer_contents.append(cursor.value)
          cursor = cursor.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
