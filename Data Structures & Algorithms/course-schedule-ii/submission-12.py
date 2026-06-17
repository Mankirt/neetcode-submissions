class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        d = defaultdict(list)

        for src, des in prerequisites:
            d[src].append(des)
        
        result = []
        visit = set()
        complete = set()
        def dfs(node):
            if node in visit:
                return False
            if node in complete:
                return True
            
            visit.add(node)
            for neigh in d[node]:
                if not dfs(neigh): return False
            visit.remove(node)
            d[node] = []
            complete.add(node)
            result.append(node)
            return True
        

        for crs in range(numCourses):
            if not dfs(crs): return []
        
        return result