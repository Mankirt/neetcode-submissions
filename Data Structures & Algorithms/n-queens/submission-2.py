class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."]*n for i in range(n)]
        ans = []
        col = set()
        diag1 = set()
        diag2 = set()
        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                ans.append(copy)
                return True
            
            
            for c in range(n):
                if c in col or (r+c) in diag1 or (r-c) in diag2:
                    continue
                col.add(c)
                diag1.add(r+c)
                diag2.add(r-c)
                board[r][c] = 'Q'
                
                backtrack(r+1)
                
                col.remove(c)
                diag1.remove(r+c)
                diag2.remove(r-c)
                board[r][c] = '.'
        backtrack(0)
        return ans
                    
