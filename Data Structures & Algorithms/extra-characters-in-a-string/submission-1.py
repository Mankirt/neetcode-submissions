class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dictionary = set(dictionary)
        dp = {len(s):0}
        def backtrack(i):

            if i in dp:
                return dp[i]
            
            res = 1 + backtrack(i+1)

            for j in range(i,len(s)):
                if s[i:j+1] in dictionary:
                    res = min(res, backtrack(j+1))
            dp[i] = res
            return res

        return backtrack(0)