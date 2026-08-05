class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        dp = {(len(nums),target):1}
        def check(i, crr):
            if (i,crr) in dp:
                return dp[(i,crr)]
            if i == len(nums):
                return 0
            res = check(i+1, crr - nums[i]) + check(i+1, crr + nums[i])
            dp[(i,crr)] = res
            return res
        
        return check(0,0)
