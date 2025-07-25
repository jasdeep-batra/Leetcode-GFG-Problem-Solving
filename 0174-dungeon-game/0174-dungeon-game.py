class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m,n = len(dungeon),len(dungeon[0])
        dp = [[0]*n for i in range(m)]
        dp[m-1][n-1] = max(1,1-dungeon[m-1][n-1])
        for j in range(n-2,-1,-1):
            dp[m-1][j] = max(1,dp[m-1][j+1]-dungeon[m-1][j])
        for i in range(m-2,-1,-1):
            dp[i][n-1] = max(1,dp[i+1][n-1]-dungeon[i][n-1])

        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                minPower = min(dp[i+1][j],dp[i][j+1])
                dp[i][j] = max(1,minPower - dungeon[i][j])   #how this formula arrived (we need next cell energy for sure so minPower is the min power among two path)

        return dp[0][0]
