class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        def backtrack(i,crr,arr):
            if crr == target:
                ans.append(arr.copy())
                return
            if i == len(nums) or crr > target:
                return
            
            arr.append(nums[i])
            backtrack(i+1,crr+nums[i],arr)
            arr.pop()
            while i+1 < len(nums) and nums[i+1] == nums[i]:
                i+=1

            backtrack(i+1,crr,arr)
            return
        
        backtrack(0,0,[])
    
        return ans