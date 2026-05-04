class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = [0,1]

        for i in range(len(s)-1):
            l = i
            r = i
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
            if r-l-1>res[1]-res[0]:
                res = [l+1,r]
            
           
            if s[i] == s[i+1]:
                l=i
                r = i+1
                while l>=0 and r<len(s) and s[l]==s[r]:
                    l-=1
                    r+=1
                if r-l-1>res[1]-res[0]:
                    res = [l+1,r]
        
        return s[res[0]:res[1]]
                
