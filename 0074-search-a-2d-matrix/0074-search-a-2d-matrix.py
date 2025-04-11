class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #since it is sorted can we apply binary search
        #and binary search returns result in log(m) TC
        i = 0
        n = len(matrix)
        m = len(matrix[0])
        j = n*m-1
        while j>=i:
            mid = (i+j)//2
            row = mid//m
            col = mid%m
            # print(mid,": ",row,":",col)
            if matrix[row][col]==target:
                return True
            if target < matrix[row][col]:
                j = mid-1
                # print("if",j)
            else:
                i = mid+1
                # print("else",i)
        return False






        