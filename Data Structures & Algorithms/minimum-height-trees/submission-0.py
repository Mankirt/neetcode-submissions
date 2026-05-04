class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1:
            return [0]
        d = defaultdict(list)

        for u,v in edges:
            d[u].append(v)
            d[v].append(u)
        


        leaves = []
        count = {}
        for key in d:
            if len(d[key])==1:
                leaves.append(key)
            count[key] = len(d[key])
        
        while leaves:
            if n<=2:
                return leaves
            
            for i in range(len(leaves)):
                node = leaves.pop(0)
                n-=1
                for neigh in d[node]:
                    count[neigh] -=1
                    if count[neigh] == 1:
                        leaves.append(neigh)