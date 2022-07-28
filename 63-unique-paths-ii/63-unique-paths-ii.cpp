class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        vector<vector<int>> dp(obstacleGrid.size()+1,vector<int>(obstacleGrid[0].size()+1,0));
        
        for(int i=1;i<obstacleGrid.size()+1;i++)
        {
            for(int j=1;j<obstacleGrid[0].size()+1;j++)
            {
                if((i==1 && j==1) && obstacleGrid[i-1][j-1]!=1 )dp[i][j] = 1;
                else if(obstacleGrid[i-1][j-1]!=1)
                {
                    dp[i][j] = dp[i-1][j] + dp[i][j-1];
                }
            }
        }
        return dp[obstacleGrid.size()][obstacleGrid[0].size()];
    }
};