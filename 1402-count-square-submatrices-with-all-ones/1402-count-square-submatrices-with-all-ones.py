class Solution:
    def countSquares(self, dp: List[List[int]]) -> int:
        summ = 0
        m,n = len(dp),len(dp[0])
        for i in range(0,m):
            if dp[i][0]==0:
                continue
            summ+=1
        for i in range(1,n):
            if dp[0][i]==0:
                continue
            summ+=1

        for i in range(1,m):
            for j in range(1,n):
                if dp[i][j]==1:
                    dp[i][j] = 1 + min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
                    summ+=dp[i][j]
        return summ


        