class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return max(nums)
        nums.append(0)
        
        print(len(nums))
        for i in range(len(nums)-4,-1,-1):
            print(i)
            nums[i] = max(nums[i]+nums[i+2],nums[i]+nums[i+3])
        
        return max(nums[0],nums[1])