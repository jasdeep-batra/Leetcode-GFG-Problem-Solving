class Solution:
    def firstSol(self,grid,i,j,summ,maxx):
        if i==len(grid) and j==len(grid):
            maxx[0] = min(maxx[0],summ)
            return

        if i>=len(grid) or j>=len(grid) or i<0 or j<0:
            return
        grid[i][j] += summ
        self.firstSol(grid,i+1,j,grid[i][j])
        self.firstSol(grid,i,j+1,grid[i][j])
        return 
    
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[sys.maxsize]*(n+1) for i in range(m+1)]
        dp[0][1] = 0
        dp[1][0] = 0
        for i in range(1,m+1):
            for j in range(1,n+1):
                temp = grid[i-1][j-1]+min(dp[i-1][j],dp[i][j-1])
                dp[i][j] = min(dp[i][j],temp)

        for item in dp:
            print(item)
        return dp[m][n]