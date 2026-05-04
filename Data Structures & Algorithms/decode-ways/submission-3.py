class Solution:
    def numDecodings(self, s: str) -> int:
        
        def backtrack(i):
            if i == len(s):
                self.count+=1
                return
            if s[i] == '0':
                return 

            backtrack(i+1)
            if i+1 < len(s) and 10<=int(s[i:i+2])<=26:
                backtrack(i+2)
        self.count = 0
        backtrack(0)
        return self.count
            