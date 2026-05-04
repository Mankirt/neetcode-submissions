class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        d = {i:[] for i in range(numCourses)}
        for cr, pre in prerequisites:
            d[cr].append(pre)
        visit = set()
        completed = set()
        self.res = []
        def dfs(i):
            if i in visit:
                return False
            if d[i] == []:
                if i not in completed:
                    self.res.append(i)
                    completed.add(i)
                return True
            visit.add(i)
            for pre in d[i]:
                if not dfs(pre):
                    return False
            visit.remove(i)
            self.res.append(i)
            d[i] = []
            completed.add(i)
            return True



        for i in range(numCourses):
            if not dfs(i):
                return []
        return self.res