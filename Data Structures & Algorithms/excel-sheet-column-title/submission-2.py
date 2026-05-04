class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = []
        while columnNumber>0:
            x = columnNumber%26 if columnNumber%26 else 26
            ans.append(chr(x+ord('A')-1))
            columnNumber = (columnNumber-1)//26
        return "".join(ans)[::-1]