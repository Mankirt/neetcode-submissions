# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        crr=head
        while crr:
            temp=crr.next
            crr.next=prev
            prev=crr
            crr=temp
        return prev