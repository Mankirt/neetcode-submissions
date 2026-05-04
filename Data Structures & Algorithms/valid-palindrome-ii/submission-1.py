class Solution:
    def validPalindrome(self, s: str) -> bool:
        ex = 0
        l, r = 0, len(s)-1
        while l<=r:
            if s[l] != s[r]:
                ex += 1
                if ex > 1:
                    return False
                if s[l] == s[r-1]:
                    r-=1
                elif s[l+1] == s[r]:
                    l+=1
                else:
                    return False
            l+=1
            r-=1
        return True