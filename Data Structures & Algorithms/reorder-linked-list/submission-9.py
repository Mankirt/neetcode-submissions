# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dumy = ListNode(0,head)
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        crr = slow.next
        prev = None
        while crr:
            temp = crr.next
            crr.next = prev
            prev = crr
            crr = temp
        slow.next = None
        
        crr = head
        crr2 = prev

        while crr2:
            temp1 = crr.next
            temp2 = crr2.next
            crr.next = crr2
            crr2.next = temp1
            crr = temp1
            crr2 = temp2
        
        



