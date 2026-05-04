class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        arr = []

        def backtrack(i):
            if i == len(s):
                res.append(arr.copy())
                return
            
            for j in range(i,len(s)):
                if palindrome(i,j):
                    arr.append(s[i:j+1])
                    backtrack(j+1)
                    arr.pop()
        
        def palindrome(i,j):
            while i < j:
                if s[i]!=s[j]:
                    return False
                i+=1
                j-=1
            return True
        
        backtrack(0)
        return res