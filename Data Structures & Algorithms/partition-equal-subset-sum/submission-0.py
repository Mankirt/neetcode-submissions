class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if sum(nums)%2 !=0:
            return False
        target = sum(nums)//2
        d = set()
        d.add(0)
        for num in nums:
            d_copy = set()
            for i in d:
                d_copy.add(i)
                d_copy.add(i+num)
            d = d_copy
        
        if target in d:
            return True
        return False