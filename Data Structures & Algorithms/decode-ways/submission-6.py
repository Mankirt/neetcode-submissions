class Solution:
    def numDecodings(self, s: str) -> int:
        count = 0
        d = {}
        def backtrack(i):
            if i in d:
                return 1 + d[i]
            if i >= len(s):
                nonlocal count
                count += 1
                return
            if s[i] == '0':
                return
            if s[i] == '1':
                if i+1 < len(s) and s[i+1] in "1234567890":
                    backtrack(i+2)
            if s[i] == '2':
                if i+1 < len(s) and s[i+1] in '1234560':
                    backtrack(i+2)
            backtrack(i+1)
        
        backtrack(0)
        return count