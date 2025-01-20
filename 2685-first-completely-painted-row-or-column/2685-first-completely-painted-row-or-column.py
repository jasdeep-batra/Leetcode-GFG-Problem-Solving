class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        #its an question of BFS o
        #idea is once we marked the visit then we have to reach the edge considering we can only move in 4 directions
        col_count = [len(mat)]*len(mat[0])
        row_count = [len(mat[0])]*len(mat)

        mapp = {}
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                mapp[mat[i][j]] = (i,j)

        for item in arr:
            i,j = mapp[item]
            col_count[j]-=1
            row_count[i]-=1
            if row_count[i]==0 or col_count[j]==0:
                return arr.index(item)
        return -1


        