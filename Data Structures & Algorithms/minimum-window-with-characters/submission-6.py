class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        t_set = defaultdict(int)
        s_set = defaultdict(int)
        for ch in t:
            t_set[ch] += 1
        l = 0
        matches =0
        res = [len(s)+1,[]]
        for r in range(len(s)):
            if s[r] in t_set:
                s_set[s[r]] += 1
                if s_set[s[r]] <= t_set[s[r]]:
                    matches +=1
                while matches == len(t):
                    if res[0] > r-l+1:
                        res = [r-l+1,[l,r]]
                    if s[l] in s_set:
                        s_set[s[l]] -=1
                        if s_set[s[l]] < t_set[s[l]]:
                            matches -=1
                    
                    l+=1
        return s[res[1][0]:res[1][1]+1] if res[0]<len(s)+1 else ""