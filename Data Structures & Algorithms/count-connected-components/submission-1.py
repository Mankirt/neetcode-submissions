class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visit = set()
        d = defaultdict(list)
        for x,y in edges:
            d[x].append(y)
            d[y].append(x)
        count = 0
        def dfs(i,last):
            if i in visit:
                return
            visit.add(i)

            for neigh in d[i]:
                #if neigh!=last:
                    dfs(neigh,i)
            return
        
        for i in range(n):
            if i not in visit:
                dfs(i,-1)
                count+=1
        return count
