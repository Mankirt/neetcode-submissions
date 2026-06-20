class UnionFind:
    def __init__(self, n):
        self._rank = [1] * (n+1)
        self._par = [i for i in range(n+1)]
    
    def _find(self, n):
        while n!=self._par[n]:
            n = self._par[self._par[n]]
        return n

    def union(self, n1, n2):
        p1 = self._find(n1)
        p2 = self._find(n2)
        if p1 == p2:
            return False
        if self._rank[p1] > self._rank[p2]:
            self._par[p2] = p1
            self._rank[p1] += self._rank[p2]
        else:
            self._par[p1] = p2
            self._rank[p2] += self._rank[p1]
        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges))
        for u,v in edges:
            if not uf.union(u, v):
                return [u,v]