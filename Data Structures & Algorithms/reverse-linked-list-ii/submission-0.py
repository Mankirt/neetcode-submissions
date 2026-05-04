# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        crr = dummy
        for i in range(left-1):
            crr =crr.next
        node1 = crr
        crr =  crr.next
        node2 = crr
        prev = None
        for i in range(right-left+1):
            temp = crr.next
            crr.next = prev
            prev = crr
            crr=temp
        node1.next.next = crr
        node1.next = prev
        return dummy.next