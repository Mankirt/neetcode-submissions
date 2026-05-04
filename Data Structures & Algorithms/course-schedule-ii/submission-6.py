class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        d = defaultdict(list)
        visit = set()
        for src, des in prerequisites:
            d[src].append(des)
        ans = []
        done = set()


        def check(i):
            if i in visit:
                return False
            if i in done:
                return True
            visit.add(i)
            result = True
            for preq in d[i]:
                if not check(preq):
                    result = False
                    break
            visit.remove(i)
            if result:
                done.add(i)
                ans.append(i)
            return result



        for i in range(numCourses):
            
                if not check(i):
                    return []
    
        return ans