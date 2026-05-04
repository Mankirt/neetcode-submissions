class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)

        def rotate(l,r):
            while l<r:
                nums[l], nums[r] = nums[r], nums[l]
                l+=1
                r-=1
            

        rotate(0,len(nums)-k-1)
        rotate(len(nums)-k,len(nums)-1)
        rotate(0, len(nums)-1)

        
