class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2: return False

        target = sum(nums)/2
        dp = {} # i, crr
        def backtrack(i, crr):
            if crr == target:
                return True
            if (i,crr) in dp: return dp[(i,crr)]
            if i == len(nums) or crr > target:
                return False
            
            res =  backtrack(i+1, crr) or backtrack(i+1, crr + nums[i])
            dp[(i,crr)] = res
            return res
        
        return backtrack(0,0)