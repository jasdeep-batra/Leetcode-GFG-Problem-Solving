class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        vector<vector<int>> dp(coins.size()+1,vector<int>(amount+1,0));
        //we need to initilize first row with INT_MAX;
        for(int i=1;i<amount+1;i++)
        {
            dp[0][i] = INT_MAX-1;
        }
        for(int i=1;i<coins.size()+1;i++)
        {
            for(int j=1;j<amount+1;j++)
            {
                if(j>=coins[i-1])
                {
                    dp[i][j] = min(1+dp[i][j-coins[i-1]],dp[i-1][j]);
                }
                else
                {
                    dp[i][j] = dp[i-1][j];
                }
            }
        }
        int ans = dp[coins.size()][amount];
        if(ans>=INT_MAX-1)return -1;
        return ans;
    }
};