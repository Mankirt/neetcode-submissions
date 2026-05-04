class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        d = defaultdict(set)
        for des, src in prerequisites:
            d[src].add(des)
        
        def dfs(crr):
            if crr in visit:
                return d[crr]

            for neigh in list(d[crr]):
                d[crr] = d[crr] | dfs(neigh)
            
            visit.add(crr)
            return d[crr]
        visit = set()
        for i in range(numCourses):
            if i not in visit:
                dfs(i)
        ans = []
        for target, key in queries:
            ans.append(target in d[key])
        
        return ans