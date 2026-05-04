class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = {}
        for i,v in enumerate(s):
            d[v] = i
        
        l,r = 0,d[s[0]]
        ans = []
        while r <len(s):
            start = l
            while l<=r:
                r = max(r,d[s[l]])
                l+=1
            ans.append(r-start+1)
            if l>=len(s):
                break
            r = d[s[l]]
        return ans

        