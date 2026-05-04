class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        arr = []
        def backtrack(i):
            if i == len(nums):
                ans.append(arr.copy())
                return
            
            arr.append(nums[i])
            backtrack(i+1)
            arr.pop()
            while i+1<len(nums) and nums[i+1] == nums[i]:
                i+=1
            backtrack(i+1)
            return
        
        backtrack(0)
        return ans
            