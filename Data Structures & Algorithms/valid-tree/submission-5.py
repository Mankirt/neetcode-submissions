class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visit = set()
        d = {i:[] for i in range(n)}
        for src,des in edges:
            d[src].append(des)
            d[des].append(src)
        def dfs(i, prev):
            if i in visit:
                return False
            visit.add(i)
            for neigh in d[i]:
                if neigh!=prev:
                    if not dfs(neigh,i):
                        return False
            return True
                    
        return dfs(0, -1) and len(visit)==n