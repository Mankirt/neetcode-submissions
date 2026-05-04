class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        x = 0
        n = len(nums)+1
        for i in range(n):
            x ^= i
            if i == len(nums):
                continue
            x ^= nums[i]

        return x