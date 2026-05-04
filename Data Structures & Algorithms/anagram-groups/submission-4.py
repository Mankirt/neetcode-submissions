class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for st in strs:
            sort = sorted(st)
            res[tuple(sort)].append(st)
        
        return list(res.values())