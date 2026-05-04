class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, n):
        while n != self.par[n]:
            self.par[n] = self.par[self.par[n]]
            n = self.par[n]
        return n

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        
        return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        for i, value in enumerate(edges):
            edges[i].append(i)
        
        edges.sort(key = lambda x:x[2])

        #Finding MST
        mst_weight = 0
        uf = UnionFind(n)
        for v1,v2,wt,i in edges:
            if uf.union(v1,v2):
                mst_weight += wt
        
        critical = []
        pse = []

        #Checking critical/pse edge
        for v1, v2, wt, i in edges:
            uf = UnionFind(n)
            mst_wt = 0
            #Skip edge
            for v3, v4, wt2, j in edges:
                if i!=j and uf.union(v3,v4):
                    mst_wt += wt2
            if max(uf.rank)!= n or mst_wt > mst_weight:
                critical.append(i)
                continue

            uf = UnionFind(n)
            mst_wt = wt
            uf.union(v1,v2)
            for v3, v4, wt2, j in edges:
                if uf.union(v3,v4):
                    mst_wt += wt2
            if mst_wt == mst_weight:
                pse.append(i)
        
        return [critical, pse]
            







































