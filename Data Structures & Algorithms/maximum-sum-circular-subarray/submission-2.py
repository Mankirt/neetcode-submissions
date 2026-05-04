class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        crrMax ,crrMin, globalMax, globalMin = nums[0], nums[0], nums[0], nums[0]

        total = nums[0]

        for i in range(1, len(nums)):
            crrMax = max(crrMax + nums[i], nums[i])
            crrMin = min(crrMin + nums[i], nums[i])
            total += nums[i]
            globalMax = max(globalMax, crrMax)
            globalMin = min(globalMin, crrMin)
        

        return max(total - globalMin, globalMax) if globalMax > 0 else globalMax