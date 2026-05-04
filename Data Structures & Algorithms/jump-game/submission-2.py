class Solution:
    def canJump(self, nums: List[int]) -> bool:
        crr = nums[0]

        for i in range(1,len(nums)):
            if i>crr:
                return False
            crr = max(crr,i+nums[i])
            if crr >= len(nums):
                break
        return True