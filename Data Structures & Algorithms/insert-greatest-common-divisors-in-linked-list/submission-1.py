# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def find(a,b):
            while a%b:
                temp = b
                b = a%b
                a = temp
            return b
        
        dummy = ListNode(0,head)
        prev = head
        crr = head.next

        while crr:
            temp = ListNode(find(prev.val,crr.val),crr)
            prev.next = temp
            prev = crr
            crr = crr.next
        
        return head
