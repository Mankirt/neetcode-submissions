class ListNode:

    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next
class MyHashSet:

    def __init__(self):
        self.hashset = [ListNode() for i in range(10000)]
        self.k = 10000

    def add(self, key: int) -> None:
        ind = key % self.k
        crr = self.hashset[ind]
        while crr.next:
            if crr.next.val == key:
                return
            crr = crr.next
        crr.next = ListNode(key)
            


    def remove(self, key: int) -> None:
        ind = key % self.k
        crr = self.hashset[ind]
        while crr.next:
            if crr.next.val == key:
                crr.next = crr.next.next
                return
            crr = crr.next
        

    def contains(self, key: int) -> bool:
        ind = key % self.k
        crr = self.hashset[ind]
        while crr.next:
            if crr.next.val == key:
                return True
            crr = crr.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)