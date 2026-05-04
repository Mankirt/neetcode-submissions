class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        s = 0
        res = len(nums) +1
        for r in range(len(nums)):
            s += nums[r]
            print(s)
            while l<=r and s>=target:
                res = min(res,r-l+1)
                s-=nums[l]
                l+=1

        return res if res!=len(nums)+1 else 0