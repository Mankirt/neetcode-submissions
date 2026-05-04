class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        res=nums[0]
        while l<=r:
            if nums[l]<=nums[r]:
                return nums[l]
            
            mid = l + (r-l)//2

            if nums[mid]>nums[r]:
                l=mid+1
            elif nums[mid]<nums[l]:
                r=mid
        
