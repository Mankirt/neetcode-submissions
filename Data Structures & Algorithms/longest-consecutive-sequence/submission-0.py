class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d={}
        for num in nums:
            d[num]=1
        res=0
        for num in nums:
            if num-1 not in d:
                l=0
                while num in d:
                    num+=1
                    l+=1
                res=max(res,l)
        return res