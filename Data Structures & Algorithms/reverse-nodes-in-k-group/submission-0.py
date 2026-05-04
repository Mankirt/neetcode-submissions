# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        crr=head
        count=0
        while crr:
            crr=crr.next
            count+=1
        dummy=ListNode(0,head)
        new_crr=dummy
        for i in range(count//k):
            self.reverse(new_crr,k)
            for i in range(k):
                new_crr=new_crr.next
        return dummy.next

    def reverse(self,start,m):
        prev=start
        crr=start.next
        while m>0:
            temp=crr.next
            crr.next=prev
            prev=crr
            crr=temp
            m-=1
        start.next.next=crr
        start.next=prev
        return