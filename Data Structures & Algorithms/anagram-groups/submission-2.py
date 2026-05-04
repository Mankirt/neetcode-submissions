class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for s in strs:
            temp = tuple(sorted(s))
            if temp in d:
                d[temp].append(s)
            else:
                d[temp] = [s]
        ans = []
        for key in d:
            ans.append(d[key])
        
        return ans