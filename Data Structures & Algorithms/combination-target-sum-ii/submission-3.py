class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        arr = []
        ans = []
        def backtrack(i, crr):
            if crr == target:
                ans.append(arr.copy())
                return
            
            if i == len(candidates) or crr > target:
                return

            arr.append(candidates[i])
            backtrack(i+1, crr + candidates[i])
            arr.pop()

            while i+1 < len(candidates) and candidates[i+1] == candidates [i]:
                i+=1
            
            backtrack(i+1, crr)

        backtrack(0,0)
        return ans