class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incoming = defaultdict(int)
        out = defaultdict(int)

        for t1,t2 in trust:
            incoming[t2] +=1
            out[t1] +=1
        
        for i in range(1,n+1):
            if incoming[i] == n-1 and out[i] == 0:
                return i
        return -1