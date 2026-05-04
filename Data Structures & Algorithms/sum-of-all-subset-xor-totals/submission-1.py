class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.s = 0

        def backtrack(i, crr):
            if i == len(nums):
                self.s += crr
                return
            backtrack(i+1,crr)
            backtrack(i+1,crr^nums[i])
        
        backtrack(0,0)
        return self.s