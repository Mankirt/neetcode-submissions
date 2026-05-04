# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        crr = head

        def gcd(a,b):
            while (a%b):
                a,b = b, (a%b)
            return b

        while crr.next:
            new = ListNode(gcd(crr.val,crr.next.val))
            new.next = crr.next
            crr.next = new
            crr = new.next
        
        return head