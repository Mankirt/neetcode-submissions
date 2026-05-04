class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        
        # Step 1: Find the middle of the list using slow and fast pointers
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse the second half of the list
        second = slow.next
        slow.next = None  # End the first half
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        # Step 3: Merge the two halves
        first, second = head, prev
        while second:
            # Save the next nodes
            temp1 = first.next
            temp2 = second.next
            
            # Rearrange pointers
            first.next = second
            second.next = temp1
            
            # Move the pointers forward
            first = temp1
            second = temp2
