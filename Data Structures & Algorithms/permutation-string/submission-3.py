class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        s1_d, s2_d= [0]*26, [0]*26
        matches=0
        for i in range(len(s1)):
            s1_d[ord(s1[i])-ord("a")]+=1
            s2_d[ord(s2[i])-ord("a")]+=1
        for i in range(26):
            if s1_d[i]==s2_d[i]:
                matches+=1
        l=0
        for i in range(len(s1),len(s2)):
            if matches == 26:
                return True
            ind= ord(s2[i])-ord("a")
            s2_d[ind] +=1
            if s2_d[ind] == s1_d[ind]:
                matches+=1
            elif s2_d[ind] == s1_d[ind] +1:
                matches-=1

            ind= ord(s2[l])-ord("a")
            s2_d[ind] -=1
            if s2_d[ind] == s1_d[ind]:
                matches+=1
            elif s2_d[ind] == s1_d[ind] -1:
                matches-=1
            l+=1
        return matches == 26
        