class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = 0
        crr = 0
        n = len(nums)+1
        for i in range(n):
            total += i
            if i == len(nums):
                continue
            crr +=nums[i]

        return total-crr