class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp= {}
        def dfs(i,crr):
            if i == len(nums) and crr == target:
                return 1
            if i==len(nums):
                return 0
            
            if (i,crr) in dp:
                return dp[(i,crr)]
            
            dp[(i,crr)] = dfs(i+1,crr-nums[i]) + dfs(i+1,crr+nums[i])
            return dp[(i,crr)]
        
        return dfs(0,0)
