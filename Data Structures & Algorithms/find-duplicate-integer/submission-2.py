class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
  
        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        t= nums[0]
        while t != slow:
            t = nums[t]
            slow = nums[slow]
        
        return slow