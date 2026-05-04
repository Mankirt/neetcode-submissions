class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = mx = mn = nums[-1]

        for i in range(len(nums)-2,-1,-1):
            temp_mx = mx
            mx = max(nums[i]*mx,nums[i]*mn,nums[i])
            mn = min(nums[i],nums[i]*mn,nums[i]*temp_mx)
            ans = max(ans,mx)
        return ans
            