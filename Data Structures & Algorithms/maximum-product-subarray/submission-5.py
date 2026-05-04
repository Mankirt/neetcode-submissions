class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mx = nums[0]
        mn = nums[0]
        ans = nums[0]
        for num in nums[1:]:
            temp = mx
            mx = max(num*mx, num*mn, num)
            mn = min(num*temp,num*mn, num)
            ans = max(ans,mx)
        
        return ans
