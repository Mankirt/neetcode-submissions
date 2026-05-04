class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return max(nums)

        a = nums[-1]
        b = nums[-2]
        c = nums[-3] + nums[-1]

        for i in range(len(nums)-4,-1,-1):
            temp = nums[i]+ max(a,b)
            a=b
            b=c
            c=temp
        
        return max(b,c)