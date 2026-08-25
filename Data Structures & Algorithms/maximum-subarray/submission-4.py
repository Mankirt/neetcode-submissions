class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        crr = 0
        res = nums[0]
        for num in nums:
            if crr + num < num:
                crr = 0
            crr += num
            res = max(res,crr)
        
        return res