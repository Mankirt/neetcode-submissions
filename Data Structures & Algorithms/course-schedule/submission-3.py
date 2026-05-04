class Solution:
    def canFinish(self, numCourses: int, pre: List[List[int]]) -> bool:
        adj = defaultdict(list)

        for a,b in pre:
            adj[a].append(b)
        
        def check(node):
            if node in visit:
                return False
            if node not in adj:
                return True
            visit.add(node)
            for prereq in adj[node]:
                if not check(prereq):
                    return False
            visit.remove(node)
            del adj[node]
            return True
        
        visit = set()
        for i in range(numCourses):
            if not check(i): return False

        return True