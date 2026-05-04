class Solution:
    def findOrder(self, numCourses: int, pre: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        res= []
        for a,b in pre:
            d[a].append(b)
        
        visit = set()
        completed = set()

        def dfs(node):
            if node in visit:
                return False
            
            if node in completed:
                return True
            
            visit.add(node)
            
            for prereq in d[node]:
                if not dfs(prereq):
                    return False
            visit.remove(node)
            res.append(node)
            completed.add(node)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
            

        return res