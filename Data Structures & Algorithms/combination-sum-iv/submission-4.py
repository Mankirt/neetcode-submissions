class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = {target: 1}
        def backtrack(crr):
            if crr in dp:
                return dp[crr]
            
            if crr > target:
                return 0
            res = 0
            for j in range(len(nums)):
                res += backtrack(crr + nums[j]) 
            dp[crr] = res
            return res
        
        return backtrack(0)