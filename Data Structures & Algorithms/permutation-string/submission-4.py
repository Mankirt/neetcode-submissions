class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i = 0
        c = Counter(s1)
        while i <len(s2)-len(s1)+1:
            if Counter(s2[i:i+len(s1)]) == c:
                return True
            i+=1
        return False
        