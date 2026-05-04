class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            j = k = i
            while j>=0 and k<len(s) and s[j]==s[k]:
                count+=1
                j-=1
                k+=1
            
            j, k = i , i+1

            while j>=0 and k<len(s) and s[j]==s[k]:
                count+=1
                j-=1
                k+=1
        return count