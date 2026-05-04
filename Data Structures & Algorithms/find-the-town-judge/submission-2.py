class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        d = defaultdict(set)

        for child,par in trust:
            d[child].add(par)
        
        for i in range(1,n+1):
            if len(d[i])==0:
                for j in range(1,n+1):
                    if j == i:
                        continue
                    if i not in d[j]:
                        return -1
                return i
        return -1