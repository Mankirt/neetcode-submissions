class Solution:
    def numDecodings(self, s: str) -> int:

        dp = [0] * (len(s) + 1)
        dp[-1] = 1

        for i in range(len(s)-1,-1,-1):
            if s[i] == '0':
                dp[i] = 0
                continue
            dp[i] += dp[i+1]
            if i < len(s) - 1 and s[i] == '1':
                dp[i] += dp[i+2]
            elif  i < len(s) - 1 and s[i] == '2' and s[i+1] in ['0','1','2','3','4','5','6']:
                dp[i] += dp[i+2]
            
            

        return dp[0]




        dp = {}
        dp[len(s)] = 1
        def backtrack(i):
            if i in dp:
                return dp[i]
            if s[i] == '0':
                return 0
            res = 0
            if i < len(s) - 1 and s[i] == '1':
                res += backtrack(i+2)
            elif i < len(s) - 1 and s[i] == '2' and s[i+1] in ['0','1','2','3','4','5','6']:
                res += backtrack(i+2)
            
            res += backtrack(i+1)
            dp[i] = res
            return res
        
       
        return  backtrack(0)