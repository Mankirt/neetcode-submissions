class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = defaultdict(list)
        for src, des in prerequisites:
            d[src].append(des)
        
        def check(i):
            if i in visit:
                return False
            if d[i] == []:
                return True
            visit.add(i)
            for neigh in d[i]:
                if not check(neigh):
                    return False
            visit.remove(i)
            d[i] = []
            return True
        


        visit = set()
        for i in range(numCourses):
            if not check(i):
                return False
        return True