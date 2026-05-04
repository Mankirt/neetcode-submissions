class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges))]
        rank = [1]*len(edges)
        def find(n):
            res = par[n-1]
            while res!=par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res
        def union(n1,n2):
            p1, p2 = find(n1-1), find(n2-1)

            if p1 == p2:
                return 1
            else:
                if rank[p1] >rank[p2]:
                    par[p2] = p1
                    rank[p1] += rank[p2]
                else:
                    par[p1] = p2
                    rank[p2] += rank[p1]
                return 0
        
        for x,y in edges:
            if union(x,y):
                return [x,y]
