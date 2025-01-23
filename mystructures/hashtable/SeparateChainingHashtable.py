from mystructures.hashtable.Node import Node

class SeparateChainingHashtable:
    def __init__(self, max_length: int):
        self.max_length = max_length
        self.table = [None] * self.max_length

        self.hash_salt = 63553

    def hash(self, key: str) -> int:
        hash = 0
        for i in range(len(key)):
            hash = (hash * self.hash_salt) + ord(key[i])
        
        return hash % self.max_length
    
    def insert(self, key: str, value: str, update: bool = False) -> Node:
        index = self.hash(key)
        if self.table[index] == None:
            self.table[index] = Node(key, value)

        elif key in self.table[index].data:
            if not update:
                msg = f'Key {key} already exists in the hashtable'
                msg2 = f'\nUse the .update() method to update the value of the key {key}'
                raise Exception(msg + msg2)
            return self.update(key, value, index=index)

        elif self.table[index].data != None:    
            self.table[index].add_colision(key, value)
        
        return Node(key, value)
    
    def update(self, key: str, value: str, index: int | None = None) -> Node:
        index = self.hash(key) if index == None else index

        if self.table[index] == None:
            raise Exception('Key not found')
        
        elif key in self.table[index].data:
            self.table[index].data[key] = value
            return Node(key, value)
    
    def search(self, key: str, index: int | None = None) -> dict:
        index = self.hash(key) if index == None else index

        if self.table[index] == None:
            raise Exception('The key was not found in the hashtable')

        elif key in self.table[index].data:
            return {
                key: self.table[index].data[key]
            }

        elif key not in self.table[index].data:
            raise Exception('Key not found at index')

    def delete(self, key: str, index: int | None = None) -> dict:
        index = self.hash(key) if index == None else index

        if self.table[index] == None:
            raise Exception('The key was not found in the hashtable')

        elif key in self.table[index].data:
            data = self.table[index].data
            self.table[index] = None
            return data

        elif key not in self.table[index].data:
            raise Exception('Key not found at index')

    def show(self):
        for i in range(self.max_length):
            if self.table[i] != None:
                print(f'|{i}| {self.table[i]}|')
            else:
                print(f'|{i}| None|')
    
    def __repr__(self) -> str:
        return str(self.table)
