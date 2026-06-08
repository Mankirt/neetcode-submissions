class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        seen = set()

        def dfs(i,j,k):
            if k == len(word):
                return True
            if not 0<=i<row or not 0<=j<col or board[i][j] != word[k] or (i,j) in seen:
                return False
            seen.add((i,j))
            result =  dfs(i+1,j,k+1) or dfs(i-1,j,k+1) or dfs(i,j+1,k+1) or dfs(i,j-1,k+1)
            seen.remove((i,j))
            return result
        
        for i in range(row):
            for j in range(col):
                if dfs(i,j,0):
                    return True
        return False