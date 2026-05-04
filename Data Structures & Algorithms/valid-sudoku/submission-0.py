class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_dict=defaultdict(list)
        col_dict=defaultdict(list)
        sq_dict=defaultdict(list)

        for r in range(9):
            for c in range(9):
                if board[r][c]!=".":
                    if (board[r][c] in row_dict[r] or
                       board[r][c] in col_dict[c] or
                       board[r][c] in sq_dict[(r//3,c//3)] ):
                       return False
                    row_dict[r].append(board[r][c])
                    col_dict[c].append(board[r][c])
                    sq_dict[(r//3,c//3)].append(board[r][c])
        return True