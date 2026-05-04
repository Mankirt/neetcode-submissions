class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        crr = 0
        for num in nums:
            crr += num
            if num > crr:
                crr = num
            ans = max(ans,crr)
        return ans