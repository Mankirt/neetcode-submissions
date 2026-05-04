class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sub = []
        def backtrack(i,s):
            if s==target:
                res.append(sub.copy())
                return
            if i==len(nums) or s>target:
                return
            sub.append(nums[i])
            backtrack(i,s+nums[i])
            sub.pop()
            backtrack(i+1,s)
        
        backtrack(0,0)
        return res