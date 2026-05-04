class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        arr = []
        def backtrack(i, crr):
            if i == len(nums):
                if crr == target:
                    res.append(arr.copy())
                return
            
            if crr > target:
                return
            arr.append(nums[i])
            backtrack(i+1, crr + nums[i])
            arr.pop()
            while i+1 < len(nums) and nums[i+1] == nums[i]:
                i+=1
            backtrack(i+1, crr)
        
        backtrack(0,0)
        return res