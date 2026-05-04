class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def bracktrack(i,l):
            if i==len(nums):
                ans.append(l.copy())
                return
            l.append(nums[i])
            bracktrack(i+1,l)
            l.pop()
            bracktrack(i+1,l)
            return
        
        bracktrack(0,[])
        return ans