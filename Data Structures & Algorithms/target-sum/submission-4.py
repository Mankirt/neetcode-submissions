class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def check(i,crr):
            if i == len(nums): 
                if crr == target:
                    return 1
                return 0
            if (i,crr) in dp:
                return dp[(i,crr)]
            
            dp[(i,crr)] = check(i+1,crr+nums[i]) + check(i+1,crr-nums[i])

            return dp[(i,crr)]

        return check(0,0)