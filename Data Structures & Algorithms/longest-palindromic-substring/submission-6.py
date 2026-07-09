class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for k in range(len(s)):
            #single:
            l = r = k
            while l>=0 and r < len(s) and s[l] == s[r]:
                if len(res) < (r-l+1):
                    res = s[l:r+1]
                l -= 1
                r += 1
                
            
            #double:
            l = k
            r = k + 1
            while l>=0 and r < len(s) and s[l] == s[r]:
                if len(res) < (r-l+1):
                    res = s[l:r+1]
                l -= 1
                r += 1
            
        return res



