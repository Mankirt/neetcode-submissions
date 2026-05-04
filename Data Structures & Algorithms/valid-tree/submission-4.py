class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visit = set()
        d = {i:[] for i in range(n)}
        for src,des in edges:
            d[src].append(des)
            d[des].append(src)
        self.count = 0
        def dfs(i, prev):
            if i in visit:
                return False
            visit.add(i)
            self.count+=1
            for neigh in d[i]:
                if neigh!=prev:
                    if not dfs(neigh,i):
                        return False
            return True
                    
        return dfs(0, -1) and self.count==n