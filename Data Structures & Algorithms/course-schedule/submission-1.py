class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = defaultdict(list)
        for des,  src in prerequisites:
            d[des].append(src)

        def check(i, visit):
            if i in visit:
                return False
            if i not in d:
                return True
            visit.add(i)
            for children in d[i]:
                if not check(children, visit):
                    return False
            return True
        for i in range(numCourses):
            visit = set()
            if not check(i, visit):
                return False
        return True