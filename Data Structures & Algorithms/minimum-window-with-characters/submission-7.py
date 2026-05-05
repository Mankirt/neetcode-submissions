class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        count = Counter(t)
        res = [float('inf'),-1,-1]
        l = 0
        count_s = defaultdict(int)
        match = 0
        for r in range(len(s)):
            if s[r] in count:
                count_s[s[r]] += 1
                if count_s[s[r]] == count[s[r]]:
                    match += 1
            while match == len(count):
                if r - l + 1 < res[0]:
                    res = [r-l+1, l , r]
                if s[l] in count:
                    count_s[s[l]] -= 1
                    if count_s[s[l]] < count[s[l]]:
                        match -= 1
                l += 1
        
        return "" if res[0] == float('inf') else s[res[1]:res[2]+1]