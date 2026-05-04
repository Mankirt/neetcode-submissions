class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l = 0
        r = 0
        while l <= r and r < len(nums):
            r = max(r,nums[l]+l)
            if r >= len(nums) - 1:
                return True
            l+=1
        
        return False
