class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l <=r :
            m = l + (r-l)//2
            
            #left sorted
            if nums[m] > nums[l]:
                if nums[r] < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            #right sorted
            else:
                if nums[r] > nums[m]:
                    r = m
                else:
                    l = m + 1
        
        return nums[r]
