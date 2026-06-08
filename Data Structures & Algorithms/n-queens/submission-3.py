class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        board = [['.' for i in range(n)] for j in range(n)]

    
        col = set()
        pos_diag = set()
        neg_diag = set()
        ans = []
        def backtrack(i):
            if i == n:
                temp = []
                for r in range(n):
                    temp.append("".join(board[r]))
                print(temp)
                ans.append(temp.copy())
                return
            for j in range(n):
                if j in col or j-i in pos_diag or i+j in neg_diag:
                    continue

            
                col.add(j)
                pos_diag.add(j-i)
                neg_diag.add(i+j)
                board[i][j] = 'Q'
                backtrack(i+1)
                board[i][j] = '.'
                col.remove(j)
                pos_diag.remove(j-i)
                neg_diag.remove(i+j)

        backtrack(0)
        
        return ans
