class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        m = defaultdict(int)
        
        l = 0
        r = 0
        h = 0
        res = 0
        while r < len(s):
            m[s[r]] += 1
            if m[s[r]] > h:
                h = m[s[r]]
            while  (r-l+1) - h > k:
                m[s[l]] -=1 
                l+=1
            res= max(res,r-l+1)
            r+=1

        return res

