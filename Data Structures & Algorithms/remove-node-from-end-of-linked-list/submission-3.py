# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = ListNode(0,head)
        crr = prev
        for i in range(n):
            crr = crr.next
        ans = prev
        while crr.next:
            crr = crr.next
            prev = prev.next
        prev.next = prev.next.next
        return ans.next