class Solution:
    @staticmethod
    def search_in_matrix(row: List[int], target: int) -> bool:
        
        if not row:
            return False

        l = 0
        r = len(row)

        mid = int((l + r)/2)

        print("Row", row)
        if row[mid] == target:
            return True
        if target < row[mid]:
            return Solution.search_in_matrix(row[l:mid], target)
        elif target > row[mid]:
            return Solution.search_in_matrix(row[mid+1:r], target) if mid+1 < r else False

        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if not matrix:
            return False

        l_row = 0
        r_row = len(matrix)

        mid_row = int((l_row + r_row)/2)

        

        print("Matrix",matrix)

        
        if matrix[mid_row][0] <= target <= matrix[mid_row][-1]:
            return Solution.search_in_matrix(matrix[mid_row], target)

        elif mid_row - 1 >= l_row and matrix[l_row][0] <= target <= matrix[mid_row-1][-1]:
            return self.searchMatrix(matrix[l_row:mid_row], target)

        elif mid_row + 1 < r_row and matrix[mid_row+1][0] <= target <= matrix[r_row-1][-1]:
            return self.searchMatrix(matrix[mid_row+1:r_row], target)


        return False
        