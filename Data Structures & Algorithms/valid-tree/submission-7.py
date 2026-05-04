class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        d = defaultdict(list)
        for src, des in edges:
            d[src].append(des)
            d[des].append(src)
        visit = set()

        def dfs(crr, par):
            if crr in visit:
                return False
            visit.add(crr)
            for neigh in d[crr]:
                if neigh != par:
                    if not dfs(neigh, crr): return False
            return True
        
        return dfs(0, -1) and len(visit) == n