class Solution:
    def numDecodings(self, s: str) -> int:
        a = 1
        b = 0

        for i in range(len(s)-1,-1,-1):
            if s[i] == "0":
                temp = 0
            else:
                temp = a
            
            if i+1 < len(s) and (s[i] == '1' or (s[i]=='2' and s[i+1] in '0123456')):
                temp += b
            
            b = a
            a = temp
        
        return a