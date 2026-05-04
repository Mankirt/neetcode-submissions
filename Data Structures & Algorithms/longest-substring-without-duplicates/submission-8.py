class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        se = set()
        res = 0
        i = 0
        l = 0
        while i<len(s):
            while s[i] in se:
                se.remove(s[l])
                l+=1
            se.add(s[i])
            res = max(res,i-l+1)
            i+=1
        return res
        