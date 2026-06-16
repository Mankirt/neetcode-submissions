class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1 : return False

        d = defaultdict(list)
        for src,des in edges:
            d[src].append(des)
            d[des].append(src)

        self.count = 0

        def dfs(node, prev):
            if node in visit:
                return False
            visit.add(node)
            self.count += 1
            for neigh in d[node]:
                if neigh != prev:
                    if not dfs(neigh,node): return False
            return True

        visit = set()
        return dfs(0,-1) and self.count == n
        
        
        