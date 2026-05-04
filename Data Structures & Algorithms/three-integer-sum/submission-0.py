class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        i=0
        while i<len(nums):
            a=nums[i]
            l=i+1
            r=len(nums)-1
            while l<r:
                if a+nums[l]+nums[r]==0:
                    res.append([a,nums[l],nums[r]])
                    l+=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                elif a+nums[l]+nums[r]<0:
                    l+=1
                else:
                    r-=1
            while i<len(nums) and nums[i]==a :
                i+=1
        return res
        