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
        d={}
        while crr:
            d[crr] = Node(crr.val)
            crr=crr.next
        
        crr=head
        while crr:
            d[crr].next=d[crr.next] if crr.next else None
            d[crr].random = d[crr.random] if crr.random else None
            crr=crr.next
        
        return d[head]
