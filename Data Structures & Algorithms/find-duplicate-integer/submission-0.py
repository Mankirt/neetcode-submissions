class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast =0
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if  slow == fast:
                break
        t = 0
        while t!=slow:
            t=nums[t]
            slow=nums[slow]
        
        return t