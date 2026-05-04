# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l = ListNode()
        crr = l
        while l1 and l2:
            if l1.val < l2.val:
                crr.next = l1
                l1 = l1.next

            else:
                crr.next = l2
                l2 = l2.next
            
            crr = crr.next
        
        if l1:
            crr.next = l1
        elif l2:
            crr.next = l2
        
        return l.next
                