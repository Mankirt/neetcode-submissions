class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        crr_sum = nums[0]

        for num in nums[1:]:
            crr_sum = max(crr_sum + num, num)

            res = max(res, crr_sum)

        return res