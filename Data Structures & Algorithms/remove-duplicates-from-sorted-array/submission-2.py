class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p1 = 0
        last = -101
        for i in range(len(nums)):
            if nums[i] != last:
                nums[i], nums[p1] = nums[p1], nums[i]
                p1+=1
            last = nums[p1-1]
        return p1