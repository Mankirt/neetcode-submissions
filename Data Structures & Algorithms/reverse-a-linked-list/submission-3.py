# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        crr = head
        prev = ListNode(0,head)

        while crr:
            temp = crr.next
            crr.next = prev
            prev = crr
            crr = temp
        
        head.next = None
        return prev