# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        crr = dummy
        count = 0
        while crr.next:
            crr=crr.next
            count+=1
        loop = count//k
        prev_crr = dummy
        crr = dummy.next
        for i in range(loop):
            tail = crr
            crr, prev = self.rotate(crr,k)
            prev_crr.next = prev
            tail.next = crr
            prev_crr = tail
        
        return dummy.next
        
    
    def rotate(self,crr,k):
        prev= None
        for i in range(k):
            temp =crr.next
            crr.next = prev
            prev = crr
            crr = temp
        return crr, prev