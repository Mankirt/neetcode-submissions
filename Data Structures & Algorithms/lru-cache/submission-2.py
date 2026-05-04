class ListNode:
    def __init__(self,val,key,next=None,prev=None):
        self.val = val
        self.next = next
        self.prev = prev
        self.key = key

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.left = ListNode(0,-1)
        self.right = ListNode(0,-1,None,self.left)
        self.left.next = self.right
        self.d = {}

    def get(self, key: int) -> int:
        if key in self.d:
            self.update(self.d[key])
            return self.d[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.update(self.d[key])
            self.d[key].val = value
            return
        
        self.d[key] = ListNode(value,key,self.right,self.right.prev)
        self.cap -= 1
        self.right.prev.next = self.d[key]
        self.right.prev = self.d[key]
        if self.cap < 0:
            self.clear()
    
    def clear(self):
        node = self.left.next
        self.left.next = node.next
        node.next.prev = self.left
        del self.d[node.key]
    
    def update(self,node):
        left = node.prev
        right = node.next
        left.next = right
        right.prev = left
        node.prev = self.right.prev
        self.right.prev.next = node
        node.next = self.right
        self.right.prev= node
        
