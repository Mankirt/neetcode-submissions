class ListNode:
    def __init__(self,key,val=0,nxt=None,prev=None):
        self.val=val
        self.key = key
        self.next= nxt
        self.prev=prev

class LRUCache:
    
    def __init__(self, capacity: int):
        self.d={}
        self.l=capacity
        self.left=ListNode(-1,0)
        self.right = ListNode(-1,0)
        self.left.next = self.right
        self.right.prev = self.left
    

    def get(self, key: int) -> int:
        if key in self.d:
            self.remove(self.d[key])
            self.insert(self.d[key])
            return self.d[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.remove(self.d[key])
        self.d[key] = ListNode(key,value)
        self.insert(self.d[key])

        if len(self.d)>self.l:
            start = self.left.next
            self.remove(start)
            del self.d[start.key]
    
    def remove(self,node):
        next = node.next
        prev = node.prev
        prev.next = next
        next.prev = prev

    def insert(self,node):
        top = self.right.prev
        top.next = node
        node.prev = top
        node.next = self.right
        self.right.prev = node
            
            

