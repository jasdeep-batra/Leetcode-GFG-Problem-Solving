class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        #swapping
        # swap only last row s then rverse the final ararya

        n = len(matrix)
        for i in range(n-1):
            for j in range(n-i-1):
                # print(i,":",j)
                # print(n-i-1,":",n-j-1)
                matrix[i][j],matrix[n-j-1][n-i-1] = matrix[n-j-1][n-i-1],matrix[i][j]
        
        # for item in matrix:
        #     print(item)
        matrix.reverse()

        """
        Do not return anything, modify matrix in-place instead.
        """
        