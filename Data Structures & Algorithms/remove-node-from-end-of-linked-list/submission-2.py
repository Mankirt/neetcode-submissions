# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        crr = dummy
        temp = dummy
        for i in range(n):
            crr = crr.next
        while crr.next:
            crr = crr.next
            temp = temp.next
        temp.next = temp.next.next
        return dummy.next
