# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        while len(lists) > 1:
            new_list = []
            for i in range(0,len(lists),2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 <len(lists) else []
                l3 = ListNode(0)
                crr = l3
                while l1 and l2:
                    if l1.val < l2.val:
                        crr.next = l1
                        l1=l1.next
                    else:
                        crr.next = l2
                        l2=l2.next
                    crr = crr.next
                if l1: crr.next = l1
                if l2: crr.next = l2
                new_list.append(l3.next)
            lists = new_list
        
        return lists[0]
                 