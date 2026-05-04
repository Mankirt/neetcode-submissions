class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visit = set()
        d = defaultdict(list)

        for src,des in edges:
            d[src].append(des)
            d[des].append(src)
        
        def dfs(i):
            if i in visit:
                return
            visit.add(i)
            for neigh in d[i]:
                if neigh not in visit:
                    dfs(neigh)
        

        count = 0
        for i in range(n):
            if i not in visit:
                dfs(i)
                count+=1
                print(visit)
        return count