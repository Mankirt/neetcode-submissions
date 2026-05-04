class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = {s[i] : i for i in range(len(s))}
        st, edge = 0, 0
        ans = []
        for i,v in enumerate(s):
            edge = max(edge,d[s[i]])
            if edge == i:
                ans.append(i-st+1)
                st = i+1
        return ans
                
