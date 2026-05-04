class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2: return False
        target = sum(nums)/2
        d= {}
        def backtrack(i,crr):
            if crr == target:
                return True
            if (i,crr) in d:
                return d[(i,crr)]
            if i == len(nums):
                return False
            return backtrack(i+1,crr+nums[i]) or backtrack(i+1,crr)
        
        return backtrack(0,0)
