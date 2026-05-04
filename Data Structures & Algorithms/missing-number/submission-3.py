class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        out = len(nums)
        for i in range(len(nums)): 
            out ^= nums[i] ^ i

        return out   