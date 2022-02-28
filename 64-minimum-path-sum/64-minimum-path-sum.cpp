class Solution {
public:
    int dp[201][201];
    int recursion(vector<vector<int>>& grid, int i, int j)
    {
        if(i==0 && j==0)
        {
            return grid[i][j];
        }
        if(i<0||j<0)return INT_MAX/2;
        if(dp[i][j]==-1)
        {
            int left = grid[i][j]+recursion(grid,i-1,j);
            int right = grid[i][j]+recursion(grid,i,j-1);
            dp[i][j] = min(left,right);
            
        }
        return dp[i][j];
    }
    int minPathSum(vector<vector<int>>& grid) 
    {
        memset(dp,-1,sizeof(dp));
        int n = grid.size()-1;
        int m = grid[0].size()-1;
        return recursion(grid,n,m);
    }
};