"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        crr=head
        d={None : None}
        while crr:
            d[crr] = Node(crr.val)
            crr=crr.next
        
        crr=head
        while crr:
            d[crr].next=d[crr.next] 
            d[crr].random = d[crr.random] 
            crr=crr.next
        
        return d[head]
