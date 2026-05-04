class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        par = [i for i in range(n)]
        rank = [1] * n
        
        def find(n):
            while par[n] != n:
                par[n] = par[par[n]]
                n = par[n]
            return n

        def union(n1, n2):
            p1 = find(n1)
            p2 = find(n2)
            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                rank[p1] += rank[p2]
                par[p2] = p1
            else:
                rank[p2] += rank[p1]
                par[p1] = p2
            return True
        
        res = n

        for u, v in edges:
            if union(u,v):
                res -= 1
        return res

            