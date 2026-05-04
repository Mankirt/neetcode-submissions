class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        for num in nums:
            if not num-1 in nums:
                crr = 1
                while num + 1 in nums:
                    num += 1
                    crr += 1
                res = max(res, crr)
        
        return res