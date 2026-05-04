class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        crr = 0
        for num in nums:
            if num > num + crr:
                crr = num
            else:
                crr += num
            ans = max(ans,crr)
        return ans