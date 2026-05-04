class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m = len(matrix) + 1
        n = len(matrix[0]) + 1

        self.sum_matrix = [[0 for i in range(n)] for i in range(m)]

        for i in range(1,m):
            crr = 0
            for j in range(1,n):
                crr +=  matrix[i-1][j-1]
                self.sum_matrix[i][j] = self.sum_matrix[i-1][j] + crr
        print(self.sum_matrix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        return self.sum_matrix[row2+1][col2+1] + self.sum_matrix[row1][col1] - self.sum_matrix[row1][col2+1] - self.sum_matrix[row2+1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)