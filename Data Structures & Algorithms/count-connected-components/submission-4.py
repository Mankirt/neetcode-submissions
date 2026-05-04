class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        com = 0
        visit = set()

        def dfs(i):
            if i in visit:
                return
            visit.add(i)

            for neigh in d[i]:
                if neigh not in visit:
                    dfs(neigh)
            
            return
        
        d = defaultdict(list)

        for src,des in edges:
            d[src].append(des)
            d[des].append(src)
        
        for i in range(n):
            if i not in visit:
                dfs(i)
                com += 1
        
        return com