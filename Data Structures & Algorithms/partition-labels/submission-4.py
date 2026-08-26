class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        index = {}
        for i,ch in enumerate(s):
            index[ch] = i
        
        start = 0
        l = 0
        r = 0
        last = 0
        ans = []
        while r < len(s):
            while l <= r:
                last = max(last,index[s[l]])
                l += 1
            if last == r:
                ans.append(r-start+1)
                start = l
                r = l
                continue
            r = last
        return ans