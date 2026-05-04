class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pt1 = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[pt1] = nums[i]
                pt1+=1
        return pt1