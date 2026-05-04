class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."]*n for i in range(n)]
        col = set()
        posDiag = set()
        negDiag = set()

        res = []
        def backtrack(i):
            if i == n:
                temp =[]
                for row in board:
                    row_data = "".join(row)
                    temp.append(row_data)
                res.append(temp)
                return
            
            for j in range(n):
                if j in col or (i-j) in negDiag or (i+j) in posDiag:
                    continue
                
                col.add(j)
                posDiag.add((i+j))
                negDiag.add((i-j))
                board[i][j] = 'Q'
                backtrack(i+1)

                col.remove(j)
                posDiag.remove((i+j))
                negDiag.remove((i-j))
                board[i][j] = '.'
        backtrack(0)
        print(res)
        return res