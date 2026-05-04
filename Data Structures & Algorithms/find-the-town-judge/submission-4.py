class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted_by = defaultdict(list)
        trusting_others = defaultdict(list)


        for t1, t2 in trust:
            trusting_others[t1].append(t1)
            trusted_by[t2].append(t1)
        
        for guy in trusted_by:
            if len(trusted_by[guy]) == n - 1 and len(trusting_others[guy])==0:
                return guy
        
        return -1


