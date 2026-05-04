class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l=0
        r=(len(matrix)*len(matrix[0]))-1
        C= len(matrix[0])
        while l<=r:
            mid = l + (r-l)//2
            col = mid%C
            row = mid//C
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                r = mid - 1
            else:
                l = mid + 1

        return False