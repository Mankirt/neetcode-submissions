class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        l = 0
        res = 1
        max_fre = 0
        for r in range(len(s)):
            count[s[r]] += 1
            max_fre = max(max_fre,count[s[r]])
            while (r-l+1) - max_fre > k:
                count[s[l]] -=1
                l+=1
            res = max(res,r-l+1)
        
        return res
