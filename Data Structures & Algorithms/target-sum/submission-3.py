class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        dp = [defaultdict(int) for i in range(len(nums)+1)]

        dp[0][0] = 1

        for i in range(1,len(nums)+1):
            for crr_sum, n in dp[i-1].items():
                dp[i][crr_sum-nums[i-1]] += n
                dp[i][crr_sum+nums[i-1]] += n
        
        return dp[len(nums)][target]