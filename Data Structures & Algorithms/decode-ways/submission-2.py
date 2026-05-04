class Solution:
    def numDecodings(self, s: str) -> int:
        self.count = 0

        def check(i):
            if i == len(s):
                self.count+=1
                return
            if s[i] == '0':
                return

            
            
            if i+1<len(s) and 10<=int(s[i:i+2])<=26:
                    check(i+2)
            
            check(i+1)
            return
        
        check(0)
        return self.count