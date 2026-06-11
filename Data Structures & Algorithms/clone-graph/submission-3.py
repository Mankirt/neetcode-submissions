"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return node
        copy_map = {}
        
        q = [node]
        visit = set()
        visit.add(node)
        while q:
            n = q.pop()
            copy_map[n] = Node(n.val)
            for neigh in n.neighbors:
                if neigh not in visit:
                    q.append(neigh)
                    visit.add(neigh)
        
        q = [node]
        visit = set()
        visit.add(node)

        while q:
            n = q.pop()
            for neigh in n.neighbors:
                copy_map[n].neighbors.append(copy_map[neigh])
                if neigh not in visit:
                    q.append(neigh)
                    visit.add(neigh)
        return copy_map[node]
 