class Solution:
    def numDecodings(self, s: str) -> int:
        count = 0
        d = {len(s): 1}
        def backtrack(i):
            if i in d:
                return d[i]
            
            if s[i] == '0':
                return 0
            
            res = backtrack(i+1)
            if i+1 < len(s) and (s[i] == '1' or s[i] == '2' and s[i+1] in '1234560'):
                    res += backtrack(i+2)
            
            d[i] = res
            return res
        
        return backtrack(0)
 