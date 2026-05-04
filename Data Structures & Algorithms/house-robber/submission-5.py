class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        a = 0
        b= 0 
        c = 0
        for i in range(len(nums)-1, -1 ,-1):
            nums[i] = nums[i] + max(a,b)
            a = b
            b = c
            c = nums[i]
        return max(nums[0],nums[1]) 