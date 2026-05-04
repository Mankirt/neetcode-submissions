class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        #Right pass
        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]
        
        #Left pass
        prev = nums[-1]
        for i in range(len(nums)-2,-1,-1):
            res[i] *= prev
            prev *= nums[i]

        return res   
