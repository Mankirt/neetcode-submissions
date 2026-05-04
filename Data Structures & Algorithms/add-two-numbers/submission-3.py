# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        ans = ListNode(0)
        crr = ans
        while l1 or l2 or carry:
            temp  = ListNode(0)
            crr.next = temp
            crr = crr.next
            one = l1.val if l1 else 0
            two = l2.val if l2 else 0
            s = one + two + carry
            crr.val = s % 10
            carry = s // 10
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return ans.next 
