class Solution:

    def encode(self, strs: List[str]) -> str:
        l = []
        for st in strs:
            l.append(str(len(st))+"#")
            l.append(st)
        print(l)
        return "".join(l)
    def decode(self, s: str) -> List[str]:
        i = 0
        ans = []
        while i<len(s):
            temp = 1
            while s[i+temp]!='#':
                temp+=1
            ind = int(s[i:i+temp])
            print(s[i+temp+1:i+temp+ind+1])
            ans.append(s[i+temp+1:i+temp+ind+1])
            i=i+temp+ind+1
        return ans