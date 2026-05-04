class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s)==0:
            return 0
        se=set()
        se.add(s[0])
        l=0
        res=1
        for r in range(1,len(s)):
            if s[r] in se:
                while s[r] in se and l<r:
                    se.discard(s[l])
                    l+=1
            se.add(s[r])
            res=max(res,len(se))

        return res