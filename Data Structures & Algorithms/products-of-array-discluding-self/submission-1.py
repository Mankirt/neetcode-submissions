class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left=[0]*len(nums)
        right=[0]*len(nums)
        prod=nums[0]
        left[0]=1


        for i in range(1,len(nums)):
            left[i]=prod
            prod*=nums[i]
        right[-1]=left[-1]
        prod=nums[-1]
        print(left)

        for i in range(len(nums)-2,-1,-1):
            right[i]=left[i]*prod
            prod*=nums[i]
        
        return right