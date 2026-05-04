class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        check_list = [0]* 26
        for ch in s1:
            check_list[ord(ch)- ord('a')] +=1
        
        final_list = [0]*26
        l = 0
        for r in range(len(s2)):
            final_list[ord(s2[r])-ord('a')] += 1
            if r>=len(s1):
                final_list[ord(s2[l])-ord('a')] -= 1
                l+=1
            if check_list == final_list:
                return True
        
        return False
        