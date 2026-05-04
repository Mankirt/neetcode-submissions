class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = s[0]
        res_l = 1

        for i in range(1,len(s)):
            j = k = i 
            while j>=0 and k<len(s) and s[j]==s[k]:
                j-=1
                k+=1
            j+=1
            k-=1
            if res_l < k-j+1:
                res_l = k-j+1
                res = s[j:k+1]
            if s[i]==s[i-1]:
                j = i-1
                k = i
                while j>=0 and k<len(s) and s[j]==s[k]:
                    j-=1
                    k+=1
                j+=1
                k-=1
                if res_l < k-j+1:
                    res_l = k-j+1
                    res = s[j:k+1]
        return res