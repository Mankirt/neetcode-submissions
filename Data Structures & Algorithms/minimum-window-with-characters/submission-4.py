class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        matches = 0
        d_t = defaultdict(int)
        d_s = defaultdict(int)
        for x in t:
            d_t[x]+=1
        l = 0
        res = len(s)+1
        ans = ""
        for i in range(len(s)):
            d_s[s[i]]+=1
            if d_s[s[i]] <= d_t[s[i]]:
                matches+=1
            while matches == len(t):
                if (i-l+1) < res:
                    res = i-l+1
                    ans = s[l:i+1]
                d_s[s[l]]-=1
                if d_s[s[l]]<d_t[s[l]]:  
                    matches-=1  
                l+=1
        return ans
                