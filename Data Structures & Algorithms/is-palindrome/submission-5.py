class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l = []
        for st in s:
            if 'a'<=st<='z' or '0'<=st<='9':
                l.append(st)
        s = "".join(l)
        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return False
            l+=1
            r-=1
        
        return True