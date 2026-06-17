class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = defaultdict(list)

        for src, des in prerequisites:
            d[src].append(des)
        
        complete = set()
        path = set()

        def dfs(node):
            if node in path:
                return False
            if node in complete:
                return True

            path.add(node)
            for neigh in d[node]:
                if not dfs(neigh): return False
            path.remove(node)
            complete.add(node)
            return True

        for crs in range(numCourses):
            if not dfs(crs) : return False

        return True   



