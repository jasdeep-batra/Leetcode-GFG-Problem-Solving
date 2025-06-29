class Solution:
    def uniquePathsWithObstacles(self, dp: List[List[int]]) -> int:
        m,n = len(dp),len(dp[0])
        if dp[0][0]==1:
            return 0
        for i in range(m):
            for j in range(n):
                if dp[i][j]==1:
                    dp[i][j] = 2
        for i in range(m):
            for j in range(n):
                if dp[i][j]==2:
                    dp[i][j]=0
                    continue
                if i==0 and j==0:
                    dp[i][j]=1
                if i-1>=0:
                    dp[i][j] += dp[i-1][j]
                if j-1>=0:
                    dp[i][j] += dp[i][j-1]
        for item in dp:
            print(dp)
        return dp[m-1][n-1]
                

        