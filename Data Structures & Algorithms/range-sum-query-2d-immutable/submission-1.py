class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row, col = len(matrix) , len(matrix[0])
        self.temp = [[0]* (col+1) for i in range(row+1)]
        for r in range(row):
            prefix = 0
            for c in range(col):
                prefix += matrix[r][c]
                self.temp[r+1][c+1] = prefix + self.temp[r][c+1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        top = self.temp[row1][col2+1]
        left = self.temp[row2+1][col1]
        overlap = self.temp[row1][col1]

        return self.temp[row2+1][col2+1] - top - left + overlap


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)