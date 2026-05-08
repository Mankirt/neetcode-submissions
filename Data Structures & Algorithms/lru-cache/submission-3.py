class Node:
    def __init__(self, key = 0, val = 0, next = None, prev = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev


class LRUCache:

    def __init__(self, capacity: int):
        self.left = Node(0,0)
        self.right = Node(0,0, None,self.left)
        self.left.next = self.right
        self.cap = capacity
        self.d = {}

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        node = self.d[key]
        self.remove(node)
        self.add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            node = self.d[key]
            self.remove(node)
            self.add(node)
            node.val = value
        else:
            node = Node(key,value)
            self.d[key] = node
            if self.cap == 0:
                del_key = self.left.next.key
                self.remove(self.left.next)
                del self.d[del_key]
                self.cap += 1
            self.add(node)
            self.cap -= 1
            

        
    def add(self, node):
        prev = self.right.prev
        prev.next = node
        self.right.prev = node
        node.next = self.right
        node.prev = prev
    
    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev
        