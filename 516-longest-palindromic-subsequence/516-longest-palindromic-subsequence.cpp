class Solution {
public:
    int longestPalindromeSubseq(string s) {
        string rs = s;
        reverse(rs.begin(),rs.end());
        int n = s.size();
        vector<vector<int>> dp(n+1,vector<int>(n+1,0));
        for(int i=1;i<n+1;i++)
        {
            for(int j=1;j<n+1;j++)
            {
                if(s[i-1]==rs[j-1])
                {
                    dp[i][j] = 1 + dp[i-1][j-1];
                }
                else
                {
                    dp[i][j] = max(dp[i][j-1],dp[i-1][j]);
                }
            }            
        }
        int ans = dp[n][n];
        return ans;
    }
};