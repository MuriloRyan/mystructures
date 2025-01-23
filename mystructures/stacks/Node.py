from typing import Any

class Node:
    def __init__(self, value: Any = None) -> None:
        self.value = value
        self.obj_type = type(self.value)
        self.next = None
    
    def _as_index(self,index):
        self.index = index

        return self

    def __repr__(self):
        return str(self.value)