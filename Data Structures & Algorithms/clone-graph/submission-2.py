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
            return node
        copy_d = defaultdict(list)

        q = [node]
        visit = set()
        visit.add(node)
        while q:
            for i in range(len(q)):
                crr = q.pop()
                copy_d[crr] = Node(crr.val)
                for neigh in crr.neighbors:
                    if neigh.val not in visit:
                        q.append(neigh)
                        visit.add(neigh.val)

        q = [node]
        visit = set()
        while q:
            for i in range(len(q)):
                crr = q.pop()
                if crr.val in visit:
                    continue
                visit.add(crr.val)
                for neigh in crr.neighbors:
                    copy_d[crr].neighbors.append(copy_d[neigh])
                    q.append(neigh)
        return copy_d[node]






