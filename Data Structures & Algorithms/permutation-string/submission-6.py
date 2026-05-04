class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        l = 0
        s1_arr = [0]*26
        s2_arr = [0]*26

        def check():
            for i in range(26):
                if s1_arr[i]!=s2_arr[i]:
                    return False
            return True

        for s in s1:
            s1_arr[ord(s) - ord('a')] +=1
        for i in range(len(s1)):
            s2_arr[ord(s2[i])-ord('a')]+=1
        if check():
            return True
        i = len(s1)
        while i <len(s2):
            s2_arr[ord(s2[i])-ord('a')]+=1
            s2_arr[ord(s2[l])-ord('a')]-=1
            l+=1
            if check():
                return True
            i+=1
        return False
    
        