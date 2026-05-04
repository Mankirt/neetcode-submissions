# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        left = dummy
        right = head

        def reverse(l,r):
            crr = l.next
            prev= r
            for i in range(k):
                temp = crr.next
                crr.next = prev
                prev = crr
                crr=temp
            l.next = prev





        for i in range(k):
            right = right.next
            if i!=k-1 and not right:
                return head
        while right:
            reverse(left,right)
            for i in range(k):
                right = right.next
                left=left.next
                if not right and i!=k-1:
                    return dummy.next
        reverse(left,right)
        return dummy.next


            
                
