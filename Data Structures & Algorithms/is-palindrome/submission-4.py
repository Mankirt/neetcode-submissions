class Solution:
    def isPalindrome(self, s: str) -> bool:
        def convert(s):
            l = []
            for i in range(len(s)):
                if (s[i] >='a' and s[i]<'z') or\
                (s[i] >='0' and s[i]<'9'):
                    l.append(s[i])
            return "".join(l)

        
        s = convert(s.lower())
        l, r = 0, len(s)-1
        while l<=r:
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True