class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[]
        def backtrack(i,l):
            if i==len(nums):
                ans.append(l.copy())
                return
            l.append(nums[i])
            backtrack(i+1,l)
            l.pop()
            while i+1<len(nums) and nums[i+1] == nums[i]:
                i+=1
            backtrack(i+1,l)
            return
        backtrack(0,[])
        return ans