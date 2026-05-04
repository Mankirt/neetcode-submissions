class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        crr= slow.next
        slow.next = prev = None
        while crr:
            temp = crr.next
            crr.next = prev
            prev = crr
            crr=temp
        crr = prev
        crr1 = head
        while crr1 and crr:
            temp1 = crr1.next
            temp2 = crr.next
            crr1.next = crr
            crr.next = temp1
            crr1 = temp1
            crr = temp2
        


