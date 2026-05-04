class ListNode:
    def __init__(self, val = None, key = None, next = None):
        self.val = val
        self.key = key
        self.next = next

class MyHashMap:

    def __init__(self):
        self.hashMap = [ListNode() for i in range(10000)]
        self.k = 10000

    def put(self, key: int, value: int) -> None:
        ind = key % self.k
        crr = self.hashMap[ind]
        while crr.next:
            if crr.next.key == key:
                crr.next.val = value
                break
            crr = crr.next
        crr.next = ListNode(value, key)

    def get(self, key: int) -> int:
        ind = key % self.k
        crr = self.hashMap[ind]
        while crr.next:
            if crr.next.key == key:
                return crr.next.val 
            crr = crr.next
        return -1
        

    def remove(self, key: int) -> None:
        ind = key % self.k
        crr = self.hashMap[ind]
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