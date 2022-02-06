class Solution {
public:
    int change(int amount, vector<int>& coins) {
      // it's a problem of dynamic programming
        //how will you recon' it?
        // some of the thing which you can observed is that 
        // they are asking for some amount. We've already seen such kind of problems lke subset sum, subset sum difference
        // here also for each element of array we have 2 choices either we should include it or exclude it 
        // moreover the range of amount will never gonna be negative... so if range is never gonna be negative
        // then there are chances that dp is applicable.
        vector<vector<int>> dp(coins.size()+1,vector<int>(amount+1,0));
        for(int i=0;i<coins.size();i++)
        {
            dp[i][0] = 1;
        }
        for(int i=1;i<coins.size()+1;i++)
        {
            for(int j=0;j<amount+1;j++)
            {
                if(j>=coins[i-1])
                {
                    dp[i][j] = dp[i][j-coins[i-1]] + dp[i-1][j];
                }
                else
                {
                    dp[i][j] = dp[i-1][j];
                }
            }
        }
        // for(int i=0;i<coins.size()+1;i++)
        // {
        //     for(int j=0;j<amount+1;j++)
        //     {
        //         cout<<dp[i][j]<<" ";
        //     }
        //     cout<<endl;
        // }
        int ans = dp[coins.size()][amount];
        return ans;
    }
};