class Solution:
    def canFinish(self, numCourses: int, prereq: List[List[int]]) -> bool:
        d = { i:[] for i in range(numCourses)}
        visit = set()
        for cr, pre in prereq:
            d[cr].append(pre)
        
        def dfs(i):
            if i in visit:
                return False
            if d[i] == []:
                return True
            visit.add(i)
            for pre in d[i]:
                if not dfs(pre):
                    return False
            visit.remove(i)
            d[i] = []
            return True

        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True