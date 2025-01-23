from typing import Any

class Node:
    def __init__(self, key: str, value: Any):
        self.data = {
            key: value
        }
    
    def add_colision(self, key: str, value: Any):
        self.data[key] = value
    
    def __str__(self) -> str:
        return str(self.data)
    
    def __repr__(self) -> str:
        return str(self.data)