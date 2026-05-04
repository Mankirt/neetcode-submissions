class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cd=defaultdict(list)
        for st in strs:
            c= [0]* 26
            for ch in st:
                c[ord(ch)-ord("a")]+=1
            cd[tuple(c)].append(st)
        return cd.values()
        
            
