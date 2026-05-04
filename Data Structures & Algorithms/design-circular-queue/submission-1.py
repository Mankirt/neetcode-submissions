class ListNode:
    def __init__(self, val= 0, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

class MyCircularQueue:

    def __init__(self, k: int):
        self.left = ListNode()
        self.right = ListNode(prev = self.left)
        self.left.next = self.right
        self.length = 0
        self.cap = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        node = ListNode(value,prev = None, next = self.right)
        prev_node = self.right.prev
        prev_node.next = node
        self.right.prev = node
        self.cap -= 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        node = self.left.next
        next_node = node.next
        self.left.next = next_node
        next_node.prev = self.left
        self.cap += 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.left.next.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.right.prev.val

    def isEmpty(self) -> bool:
        if self.left.next == self.right:
            return True
        return False

    def isFull(self) -> bool:
        if self.cap == 0:
            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()