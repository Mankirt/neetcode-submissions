class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        arr = []
        ans = []
        dp = {}
        def dfs(i):
            if i == len(s):
                ans.append(" ".join(arr))
                return
            
            for j in range(i+1, len(s)+1):
                if s[i:j] in wordDict:
                    arr.append(s[i:j])
                    dfs(j)
                    arr.pop()
        
        dfs(0)
        return ans
