class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        arr = []

        def backtrack(i):

            if i == len(s):
                ans.append(arr.copy())
                return
            
            for j in range(i,len(s)):
                if palindrome(s[i:j+1]):
                    arr.append(s[i:j+1])
                    backtrack(j+1)
                    arr.pop()
        
        def palindrome(s):
            if s == s[::-1]:
                return True
            return False
        
        backtrack(0)
        return ans