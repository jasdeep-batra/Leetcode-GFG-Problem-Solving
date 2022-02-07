class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        vector<vector<int>> dp(text1.size()+1, vector<int>(text2.size()+1,0));
        int n1 = text1.size();
        int n2 = text2.size();        
        for(int i=1;i<n1+1;i++)
        {
            for(int j=1;j<n2+1;j++)
            {
                if(text1[i-1]==text2[j-1])
                {
                    dp[i][j] = 1 + dp[i-1][j-1];
                }
                else
                {
                    dp[i][j] = max(dp[i][j-1] , dp[i-1][j]);
                }
            }
        }
        int ans = dp[n1][n2];
        return ans;
    }
};