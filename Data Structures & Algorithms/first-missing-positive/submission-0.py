class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        l = len(nums)

        for i in range(l):
            if nums[i] < 0 :
                nums[i] = 0
        for i in range(l):
            val = abs(nums[i])
            if 1<=val<=(l):
                if nums[val-1] > 0 :
                    nums[val-1] *= -1
                elif nums[val-1] == 0:
                    nums[val-1] = -(l+2)

        for i in range(l):
            if nums[i] >= 0:
                return i+1
        
        return  l+1
                    