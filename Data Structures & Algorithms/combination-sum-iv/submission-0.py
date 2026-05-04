class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = {target:1}
        def check(crr):
            if crr in dp:
                return dp[crr]
            if crr > target:
                return 0
            ans = 0
            for j in range(len(nums)):
                ans += check(crr+nums[j])
            dp[crr] = ans
            return ans
        return check(0)