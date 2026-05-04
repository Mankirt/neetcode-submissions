class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans =[]
        temp =[]
        def backtrack(i):
            if i==len(s):
                ans.append(temp.copy())
                return

            for j in range(i,len(s)):
                if check(i,j):
                    temp.append(s[i:j+1])
                    backtrack(j+1)
                    temp.pop()
        def check(i,j):
            while i<=j:
                if s[i]!=s[j]:
                    return False
                i+=1
                j-=1
            return True
        
        backtrack(0)
        return ans
            