class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for k in range(len(s)):
            #single:
            l = r = k
            while l>=0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
                
            
            #double:
            l = k
            r = k + 1
            while l>=0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            
        return res