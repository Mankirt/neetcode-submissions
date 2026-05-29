class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        arr = []
        ans = []
        def backtrack(i, crr):

            if crr == target:
                ans.append(arr.copy())
                return
            if crr > target or i == len(nums):
                return

            arr.append(nums[i])
            backtrack(i, crr + nums[i])

            arr.pop()
            backtrack(i+1, crr)
        
        backtrack(0,0)
        return ans
