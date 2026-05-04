class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d={'2':'abc','3':"def",'4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs','8':'tuv','9':'wxyz'}
        res = []
        temp = []
        def backtrack(i):
            if i==len(digits):
                if temp:
                    res.append("".join(temp))
                return
            
            for n in d[digits[i]]:
                temp.append(n)
                backtrack(i+1)
                temp.pop()
        
        backtrack(0)
        return res
            