class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = {}
        for i, ch in enumerate(s):
            d[ch] = i
        
        ans = []
        start = 0
        last = 0
        for i in range(len(s)):
            last = max(last,d[s[i]])
            if i == last:
                ans.append(i-start+1)
                last = i+1
                start = i+1
            
        
        return ans