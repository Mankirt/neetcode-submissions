class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        max_res = max(len(word1), len(word2))
        dp = [[max_res] * (len(word2)+1) for i in range(len(word1) + 1)]
        dp[-1][-1] = 0

        for i in range(len(word1),-1,-1):
            for j in range(len(word2),-1,-1):
                if i == len(word1) or j == len(word2):
                    dp[i][j] = max(len(word1) - i, len(word2) - j)
                    continue
                
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = 1 + min(dp[i+1][j+1], dp[i+1][j], dp[i][j+1])
        return dp[0][0]

    
        dp = {(len(word1),len(word2)):0}
        def check(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            if j == len(word2) or i == len(word1):
                return max(len(word1) - i, len(word2) - j)
            
            if word1[i] == word2[j]:
                res = check(i+1,j+1)
            else:
                res = 1 + min(check(i+1,j+1),  check(i+1,j),  check(i,j+1))
            dp[(i,j)] = res
         
            return res
        
        return check(0,0)
        

