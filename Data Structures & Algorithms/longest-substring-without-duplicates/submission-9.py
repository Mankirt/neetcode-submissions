class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = set()
        l = 0
        r = 0
        res = 0
        while r<len(s):
            while s[r] in m:
                m.remove(s[l])
                l+=1
            m.add(s[r])
            res = max(res,r-l+1)
            r+=1
        return res
