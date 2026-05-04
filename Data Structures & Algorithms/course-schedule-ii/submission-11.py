class Solution:
    def findOrder(self, numCourses: int, pre: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        res = []
        visit = set()
        completed = set()
        for src, des in pre:
            d[src].append(des)
        
        def dfs(crr):
            if crr in visit:
                return False
            if crr in completed:
                return True
            
            visit.add(crr)
            for neigh in d[crr]:
                if not dfs(neigh):
                    return False
            
            res.append(crr)
            completed.add(crr)
            visit.remove(crr)
            return True

        for i in range(numCourses):
            if not dfs(i): return []
        
        return res