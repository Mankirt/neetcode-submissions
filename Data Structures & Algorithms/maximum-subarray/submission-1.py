class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        crr = nums[0]
        ans = nums[0]
        for i in range(1,len(nums)):
            if nums[i] + crr < nums[i]:
                crr = nums[i]
            else:
                crr+=nums[i]
            ans = max(ans,crr)
        
        return ans