class ListNode:
    def __init__(self, key = -1, val = -1, next = None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:

    def __init__(self):
        self.arr = [ListNode() for i in range(1000)]

    def hash(self, key):
        return key%1000

    def put(self, key: int, value: int) -> None:
        crr = self.arr[self.hash(key)]
        while crr.next:
            if crr.next.key == key:
                crr.next.val = value
                return
            crr = crr.next
        crr.next = ListNode(key,value)

    def get(self, key: int) -> int:
        crr = self.arr[self.hash(key)]
        while crr.next:
            if crr.next.key == key:
                return crr.next.val
            crr = crr.next
        return -1

    def remove(self, key: int) -> None:
        crr = self.arr[self.hash(key)]
        while crr.next:
            if crr.next.key == key:
                crr.next = crr.next.next
                return 
            crr = crr.next
    


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)