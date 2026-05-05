class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        res = 0
        visit = set()
        while r < len(s):
            while s[r] in visit:
                visit.remove(s[l])
                l += 1
            visit.add(s[r])
            res = max(res, r - l + 1)
            r += 1
        
        return res