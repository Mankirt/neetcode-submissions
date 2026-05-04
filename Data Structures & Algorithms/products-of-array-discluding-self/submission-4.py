class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        crr = 1
        output = [crr]
        for i in range(1,len(nums)):
            crr *= nums[i-1]
            output.append(crr)
        
        crr = 1
        for i in range(len(nums)-2, -1,-1):
            crr *= nums[i+1]
            output[i] *= crr
        
        return output