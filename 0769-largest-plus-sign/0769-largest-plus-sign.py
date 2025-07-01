class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        dp = [[n]*n for _ in range(n)]
        for x,y in mines:
            dp[x][y] = 0

        for i in range(n):
            count = 0
            for j in range(n):
                count = 0 if dp[i][j]==0 else count+1
                dp[i][j] = count
            
            count = 0
            for j in range(n-1,-1,-1):
                count = 0 if dp[i][j]==0 else count+1
                dp[i][j] = min(count,dp[i][j])

        for j in range(n):
            count = 0
            for i in range(n):
                count = 0 if dp[i][j]==0 else count+1
                dp[i][j] = min(dp[i][j],count)
            
            count = 0
            for i in range(n-1,-1,-1):
                count = 0 if dp[i][j]==0 else count+1
                dp[i][j] = min(count,dp[i][j])

        return max([max(item) for item in dp])