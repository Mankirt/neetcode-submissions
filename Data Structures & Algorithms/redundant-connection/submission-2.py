class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        par = [ i for i in range(n+1)]
        rank = [1] * (n+1)

        def find(a):
            if not a == par[a]:
                par[a] = find(par[a])
            return par[a]


        def union(n1,n2):
            par1, par2 = find(n1), find (n2)
            if par1 == par2:
                return False
            if rank[par1] > rank[par2]:
                par[par2] = par1
                rank[par1] += rank[par2]
            else:
                par[par1] = par2
                rank[par2] += rank[par1]
            
            return True
        
        for e1, e2 in edges:
            if not union(e1,e2):
                return [e1,e2]
            

