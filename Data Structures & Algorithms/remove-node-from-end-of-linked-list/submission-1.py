# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        crr= dummy
        for i in range(n):
            crr=crr.next
        crr1 = dummy
        while crr.next:
            crr=crr.next
            crr1=crr1.next
        crr1.next = crr1.next.next
        return dummy.next