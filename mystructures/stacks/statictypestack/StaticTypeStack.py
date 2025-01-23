from dataclasses import dataclass
from mystructures.stacks.Node import Node
from typing import Any

@dataclass
class StaticTypeStack:
    def __init__(self, exclusive_type: Any, node_class=Node) -> None:
        """ This class is a stack witch only allow you to insert objects of a specific type"""

        self.exclusive_type = exclusive_type
        self.root = node_class()

    def typecheck(self, object) -> dict:
        return {
            'result' : isinstance(object, self.exclusive_type),
            'obj_type': type(object),
            'exclusive_type': self.exclusive_type
        }
    
    def push(self, value: Any) -> bool:
        if self.typecheck(value)['result'] == True:
            current_node = self.root
            while current_node.next != None:
                current_node = current_node.next
            
            current_node.next = Node(value)
            return True

        return False
    
    def pop(self) -> bool:
        current_node = self.root
        if len(self) == 0:
            return False

        try:
            while current_node.next.next != None:
                current_node = current_node.next
            
            current_node.next = None
            return True
        
        except AttributeError:
            return False

    def __len__(self) -> int:
        current_node, i = self.root, 0

        while current_node.next:
            i+=1

            #the next node is the next node of the last one
            current_node = current_node.next
        
        #return the length 
        return i
    
    def __getitem__(self, index: int):
        if not isinstance(index, int):
            raise
        
        current_node,i = self.root.next, 0
        while i < index:
            if not current_node.next:
                raise IndexError

            current_node = current_node.next
            i += 1

        return current_node._as_index(i)
    
    def __iter__(self):
        self._iter_index = 0
        return self

    def __next__(self):
        #return Stack[i]
        try:
            value = self[self._iter_index]
            self._iter_index += 1
            return value
        
        except:
            raise StopIteration
