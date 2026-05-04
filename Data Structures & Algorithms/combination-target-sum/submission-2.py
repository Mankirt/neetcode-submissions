class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []

        def backtrack(i,crr,arr):
            if crr==target:
                ans.append(arr.copy())
                return
            if i == len(nums) or crr > target:
                return
            
            arr.append(nums[i])
            backtrack(i,crr+nums[i],arr)
            arr.pop()
            backtrack(i+1,crr,arr)
        
        backtrack(0,0,[])

        return ans