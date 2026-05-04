class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        sub = []
        def backtrack(i,s):
            if s==target:
                ans.append(sub.copy())
                return
            if s>target or i==len(candidates):
                return
            
            sub.append(candidates[i])
            backtrack(i+1,s+candidates[i])
            sub.pop()
            while i+1<len(candidates) and candidates[i+1] == candidates[i]:
                    i+=1
            backtrack(i+1,s)
        backtrack(0,0)
        return ans