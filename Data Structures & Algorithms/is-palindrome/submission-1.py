class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        l=0
        r=len(s)-1
        while l<r:
            while l< r and not self.check(s[l]):
                l+=1
            while r> l and not self.check(s[r]):
                r-=1
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True
    def check(self, c):
        return (ord('a')<=ord(c)<=ord("z") or ord('0')<=ord(c)<=ord("1"))