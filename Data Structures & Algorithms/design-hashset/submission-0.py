class ListNode:
    def __init__(self,val=-1,nxt=None):
        self.value = val
        self.nxt = nxt

class MyHashSet:

    def __init__(self):
        self.hashset = [ListNode() for i in range(10**4)]

    def add(self, key: int) -> None:
        ind = key % len(self.hashset)
        crr = self.hashset[ind]
        while crr.nxt:
            if crr.nxt.value == key:
                return
            crr = crr.nxt
        crr.nxt = ListNode(key)

    def remove(self, key: int) -> None:
        ind = key % len(self.hashset)
        crr = self.hashset[ind]
        while crr.nxt:
            if crr.nxt.value == key:
                crr.nxt = crr.nxt.nxt
                return
            crr = crr.nxt
        

    def contains(self, key: int) -> bool:
        ind = key % len(self.hashset)
        crr = self.hashset[ind]
        while crr.nxt:
            if crr.nxt.value == key:
                return True
            crr = crr.nxt
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)