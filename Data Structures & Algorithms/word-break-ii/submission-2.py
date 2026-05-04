class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        arr = []
        res = []
        def backtrack(i,j):
            if j == len(s):
                if i == j:
                    st = " ".join(arr)
                    res.append(st)
                return
            if s[i:j+1] in wordDict:
                arr.append(s[i:j+1])
                backtrack(j+1,j+1)
                arr.pop()
            backtrack(i,j+1)
            return
        backtrack(0,0)
        return res
