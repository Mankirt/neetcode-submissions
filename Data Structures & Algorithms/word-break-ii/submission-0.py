class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        s_set = set(wordDict)
        res = []
        def backtrack(i,ls,x):
            if i==len(s):
                if x==i:

                    res.append(" ".join(ls))
                return
            if s[x:i+1] in s_set:
                ls.append(s[x:i+1])
                backtrack(i+1,ls,i+1)
                ls.pop()
            backtrack(i+1,ls,x)
        backtrack(0,[],0)
        return res
