class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dict1 = set(wordDict)
        dp={len(s):True}
        def check(i,j):
            if i in dp:
                return dp[i]
            if j==len(s):
                return False
            res = False
            if s[i:j+1] in dict1:
                res = check(j+1,j+1)
            res = res or check(i,j+1)
            dp[i] = res
            return res
        return check(0,0)
            