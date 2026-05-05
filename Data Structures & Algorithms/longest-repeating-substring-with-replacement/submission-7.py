class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_fre = 0
        d = defaultdict(int)

        l = 0
        r = 0
        res = 0
        while r < len(s):
            d[s[r]] += 1
            max_fre = max(max_fre, d[s[r]])

            while r - l + 1 - max_fre > k:
                d[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

            r += 1
        
        return res