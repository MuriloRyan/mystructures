from operator import length_hint
from platform import node
from mystructures.linkedlist.Node import Node

class CircularLinkedList:
    def __init__(self):
        self.root = None

    def append(self, data):
        new_node = Node(data)

        if not self.root:
            self.root = new_node
            self.root.next = self.root

        else:
            current_node = self.root

            while current_node.next != self.root:
                current_node = current_node.next
            
            current_node.next = new_node
            new_node.next = self.root
    
    def pop(self):
        if not self.root:
            raise IndexError('pop from empty linkedlist')
        
        current_node = self.root

        if self.root.next == self.root:
            self.root = None
            return current_node
        
        if len(self) == 2:
            deleted_node = current_node.next
            current_node.next = current_node

            return deleted_node

        while current_node.next.next != self.root:
            current_node = current_node.next
        
        last_node = current_node.next
        current_node.next = self.root
    
        return last_node
    
    def find_one(self, data):
        current_node = self.root
        index = 0

        while current_node.data != data:
            current_node = current_node.next
            index += 1

            if current_node == self.root:
                raise StopIteration

        return [current_node, index]
    
    def __getitem__(self, steps):
        current_node = self.root
        i = 0

        while i <= steps:
            node = current_node
            current_node = current_node.next

            i += 1

        return node
    
    def __len__(self):
        length = 0
        for i in self:
            length += 1

        return length
    
    def __iter__(self):
        self._iter_current_node = self.root
        self._iter_started = False
        return self

    def __next__(self):
        if self._iter_current_node is None:
            raise StopIteration

        if not self._iter_started:
            self._iter_started = True
            return self._iter_current_node

        self._iter_current_node = self._iter_current_node.next

        if self._iter_current_node == self.root:
            raise StopIteration

        return self._iter_current_node
        
    def __repr__(self):
        if len(self) >= 1:
            object_list = []

            current_node = self.root
            while True:
                object_list.append(str(current_node))

                current_node = current_node.next
                if current_node == self.root:
                    break

            return f'Circular{str(object_list)}'
        return f'Circular[]'