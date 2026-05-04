class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = [1,0,0]
        for i in range(len(s)):
            #Case 1
            l = i
            r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > res[0]:
                    res = [r-l+1,l,r]
                l -= 1
                r += 1
            
            if i < len(s) - 1 and s[i] == s[i+1]:
                l = i
                r = i+1
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    if (r-l+1) > res[0]:
                        res = [r-l+1,l,r]
                    l -= 1
                    r += 1
        
        return s[res[1]:res[2]+1]


