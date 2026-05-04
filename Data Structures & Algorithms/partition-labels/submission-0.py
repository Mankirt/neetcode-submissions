class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = {}
        for i in range(len(s)):
            d[s[i]] = i
        farthest = d[s[0]]
        prev = 0
        res = []
        for i in range(1,len(s)):
            if i > farthest:
                res.append(farthest-prev+1)
                prev = i
                farthest = d[s[i]]
            else:
                farthest = max(farthest,d[s[i]])
        res.append(farthest-prev+1)
        return res
