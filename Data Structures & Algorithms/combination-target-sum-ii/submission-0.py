class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        
        ans=[]
        def backtrack(i,crr,l):

            if crr==target:
                ans.append(l.copy())
                return
            if i==len(candidates) or crr>target:
                return
            
            
            l.append(candidates[i])
            backtrack(i+1,crr+candidates[i],l)
            l.pop()
            while i+1 <len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            backtrack(i+1,crr,l)
            return
        backtrack(0,0,[])
        return ans