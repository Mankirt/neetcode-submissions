class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans=[]
        def backtrack(i,l,crr):
            if i==len(nums) or crr>target:
                return
            
            if crr == target:
                ans.append(l.copy())
                return
            
            l.append(nums[i])
            backtrack(i,l,crr+nums[i])
            l.pop()
            backtrack(i+1,l,crr)
            return
        backtrack(0,[],0)
        return ans