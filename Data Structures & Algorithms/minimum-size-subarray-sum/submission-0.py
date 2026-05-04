class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = len(nums)+1
        s = 0
        l = 0
        for i in range(len(nums)):
            s+=nums[i]
            while s>=target:
                res = min(res,(i-l+1))
                s-=nums[l]
                l+=1
        return res if res<len(nums)+1 else 0
