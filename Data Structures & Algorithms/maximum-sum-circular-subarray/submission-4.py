class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        gMax = nums[0]
        gMin = nums[0]
        crrMax = nums[0]
        crrMin = nums[0]
        total = nums[0]
        for num in nums[1:]:
            crrMax = max(crrMax + num, num)
            gMax = max(gMax, crrMax)
            total += num
            crrMin = min(crrMin + num, num)
            gMin = min(gMin, crrMin)
        
        return max(total - gMin, gMax) if gMax >= 0 else gMax