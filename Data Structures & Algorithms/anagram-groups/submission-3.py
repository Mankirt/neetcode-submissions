class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for s in strs:
            c = [0] * 26
            for ch in s:
                c[ord(ch) - ord('a')] += 1
            d[tuple(c)].append(s)
        
        ans = []

        for key in d:
            ans.append(d[key])
        
        return ans