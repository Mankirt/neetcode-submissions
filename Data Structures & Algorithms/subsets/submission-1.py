class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(i,l):
            if i==len(nums):
                ans.append(l.copy())
                return
            l.append(nums[i])
            backtrack(i+1,l)
            l.pop()
            backtrack(i+1,l)
        
        backtrack(0,[])
        return list(ans)