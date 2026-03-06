class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        i,j = matrix[0][0], matrix[-1][-1]
        def Count(target):
            i = 0
            j = len(matrix[0])-1
            count = 0
            while i<len(matrix) and j>=0:
                if target >= matrix[i][j]:
                    i+=1
                    count+=j+1
                else:
                    j-=1

            return count
        while j>i:
            mid = (j+i)//2
            cnt = Count(mid)
            if cnt >= k:
                j = mid
            else:
                i = mid+1
        
        return i