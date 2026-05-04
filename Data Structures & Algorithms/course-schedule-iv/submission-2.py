class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        d = defaultdict(list)

        for src, des in prerequisites:
            d[des].append(src)

        

        def dfs(i,x):
            if i in visit:
                return
            d[x].append(i)
            visit.add(i)
            for neigh in d[i]:
                if neigh not in visit:
                    dfs(neigh,x)
            
            


        
        for i in range(numCourses):
            visit = set()
            dfs(i,i)
        ans = []
        for u,v in queries:
            if u in d[v]:
                ans.append(True)
            else:
                ans.append(False)
        
        return ans
        
