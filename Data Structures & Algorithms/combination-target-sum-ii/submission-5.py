class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        arr = []
        ans = []
        candidates.sort()
        def backtrack(i, crr):
            if crr == target:
                ans.append(arr.copy())
                return
            if crr > target or i == len(candidates):
                return
            
            arr.append(candidates[i])
            backtrack(i+1, crr + candidates[i])

            arr.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            backtrack(i + 1, crr)
        
        backtrack(0,0)
        return ans