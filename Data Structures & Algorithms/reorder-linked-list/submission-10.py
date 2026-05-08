# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

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

        left = head
        right = prev
        while right:
            temp_left = left.next
            temp_right = right.next
            left.next = right
            right.next = temp_left
            left = temp_left
            right = temp_right
