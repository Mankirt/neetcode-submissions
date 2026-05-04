# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        prev = dummy
        l = head
        r = head
        for i in range(1,right+1):
            r = r.next
        for i in range(1,left):
            l = l.next
            prev = prev.next
        last = r
        for i in range(right-left+1):
            temp = l.next
            l.next = last
            last = l
            l = temp
        prev.next = last

        return dummy.next