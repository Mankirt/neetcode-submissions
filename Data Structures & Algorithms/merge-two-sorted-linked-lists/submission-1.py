# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == [] and list2 == []:
            return []
        if list1 == []:
            return list2
        if list2 ==[]:
            return list1

        ans=ListNode(0)
        crr=ans
        while list1 and list2:
            if list1.val < list2.val:
                crr.next=list1
                list1=list1.next
                
            else:
                crr.next=list2
                list2=list2.next
            
            crr=crr.next
        while list1:
            crr.next=list1
            list1=list1.next
            crr=crr.next
        while list2:
            crr.next=list2
            list2=list2.next
            crr=crr.next
        return ans.next
                