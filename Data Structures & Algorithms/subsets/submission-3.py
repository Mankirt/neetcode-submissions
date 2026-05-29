class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        arr = []
        ans = []
        def backtrack(i):
            if i == len(nums):
                ans.append(arr.copy())
                return
            
            arr.append(nums[i])
            backtrack(i+1)
            arr.pop()
            backtrack(i+1)
            return
        
        backtrack(0)
        return ans