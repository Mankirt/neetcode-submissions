class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        p1 = 0
        p2 = len(nums) - 1
        i = 0
        while i<=p2:
            num = nums[i]
            if num == 0:
                nums[i], nums[p1] = nums[p1] , nums[i]
                p1 += 1
            elif num == 2:
                nums[i], nums[p2] = nums[p2] , nums[i]
                p2 -= 1
                i-=1
            i+=1
        

        