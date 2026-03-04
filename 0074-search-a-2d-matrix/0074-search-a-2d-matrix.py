class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n = len(matrix),len(matrix[0])
        i = 0
        j = m*n-1
        while j >= i:
            mid = (j+i)//2
            x,y = mid//n, mid%n
            if matrix[x][y]==target:
                return True
            if matrix[x][y] > target:
                j = mid-1
            else:
                i = mid+1

        return False
