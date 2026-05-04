class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        dp = [defaultdict(int) for _ in range(len(nums) + 1)]

        dp[0][0] = 1
        for i in range(len(nums)):
            for key, val in dp[i].items():
                dp[i+1][key-nums[i]] += val
                dp[i+1][key+nums[i]] += val
        return dp[-1][target]
        
        
        
        def check(i, crr):
            if i == len(nums):
                if crr == target:
                    return 1
                return 0
            if (i,crr) in dp:
                return dp[(i,crr)]
            
            dp[(i,crr)] = check(i+1, crr - nums[i]) + check(i+1, crr + nums[i])
            return dp[(i,crr)]
        

        dp = {}
        return check(0,0)