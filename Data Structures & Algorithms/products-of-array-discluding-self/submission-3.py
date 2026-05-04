class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0]* len(nums)
        crr = 1
        right = [crr]
        for i in range(1,len(nums)):
            crr *= nums[i-1]
            right.append(crr)
        
        left = [0]*len(nums)

        left[-1] = 1
        crr = 1
        for i in range(len(nums)-2, -1,-1):
            crr *= nums[i+1]
            left[i] =crr
        
        for i in range(len(nums)):
            output[i] = left[i] * right[i]
        

        return output