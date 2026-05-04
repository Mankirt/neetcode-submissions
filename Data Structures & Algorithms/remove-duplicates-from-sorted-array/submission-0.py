class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pt = 1
        i = 1
        while i < len(nums):
            if nums[i] != nums[i-1]:
                nums[pt] = nums[i]
                pt+=1
            i+=1
        return pt