class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hash_map = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }
        ans = []
        arr = []
        def backtrack(i):
            if i == len(digits):
                if arr:
                    ans.append("".join(arr))
                return
            
            for ch in hash_map[digits[i]]:
                arr.append(ch)
                backtrack(i+1)
                arr.pop()

        backtrack(0)
        return ans