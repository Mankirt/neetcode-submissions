class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_dict=defaultdict(set)
        col_dict=defaultdict(set)
        sq_dict=defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c]!=".":
                    if (board[r][c] in row_dict[r] or
                       board[r][c] in col_dict[c] or
                       board[r][c] in sq_dict[(r//3,c//3)] ):
                       return False
                    row_dict[r].add(board[r][c])
                    col_dict[c].add(board[r][c])
                    sq_dict[(r//3,c//3)].add(board[r][c])
        return True