class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False

        count_s = [0] * 26
        for ch in s1:
            count_s[ord(ch) - ord('a')] += 1
        count_t = [0] * 26
        l = 0 
        for r in range(len(s2)):

            count_t[ord(s2[r]) - ord('a')] += 1
            if r - l + 1 > len(s1):
                count_t[ord(s2[l]) - ord('a')] -= 1
                l += 1
            match = 0
            for i in range(26):
                if count_s[i] == count_t[i]:
                    match += 1
            if match == 26: return True
        
        return False