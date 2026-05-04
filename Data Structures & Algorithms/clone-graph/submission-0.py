"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        d={}
        q=[node]
        visit= set()
        while q:
            n = q.pop(0)
            d[n] = Node(n.val)
            visit.add(n)
            for neigh in n.neighbors:
                if neigh not in visit:
                    q.append(neigh)
        visit=set()
        q=[node]
        while q:
            n = q.pop(0)
            if n not in visit:
                visit.add(n)
                for neigh in n.neighbors:
                    d[n].neighbors.append(d[neigh])
                    q.append(neigh)
        return d[node]
        