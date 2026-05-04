class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        dp = {len(s): True}
        def backtrack(i):
            if i in dp:
                return dp[i]
            res = False
            for j in range(i, len(s)):
                if s[i:j+1] in wordDict:
                    if backtrack(j+1): 
                        res = True
                        break
            dp[i] = res
            return res
        
        return backtrack(0)