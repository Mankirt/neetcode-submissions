class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = {}
        for num in nums:
            d[num] = 1
        res = 0
        for key in d:
            if key - 1 in d:
                continue
            count = 0
            while key in d:
                count += 1
                key += 1
            res = max(res, count)
        
        return res
            