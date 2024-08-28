class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        #brute force

        def dfs(i,j):
            if i<0 or j<0 or i>=len(grid2) or j>=len(grid2[0]) or grid2[i][j]==0:
                return True
            grid2[i][j] = 0

            currVisitStatus = grid1[i][j]==1
            currVisitStatus = currVisitStatus & dfs(i-1,j)
            currVisitStatus = currVisitStatus & dfs(i+1,j)
            currVisitStatus = currVisitStatus & dfs(i,j+1)
            currVisitStatus = currVisitStatus & dfs(i,j-1)
            return currVisitStatus

        ans = 0
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j]==1:
                    if dfs(i,j):
                        ans+=1

        return ans
                
            

        

        