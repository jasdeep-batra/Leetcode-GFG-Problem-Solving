class Solution {
public:
    int findMaxForm(vector<string>& strs, int m, int n) {
        // we might have to use bit manipulation
        vector<vector<int>> dp(m+1,vector<int>(n+1,0));
        for(auto s: strs)
        {
            int zc = count(s.begin(),s.end(),'0');
            int oc = s.size()-zc;
            for(int i=m;i>=zc;i--)
            {
                for(int j=n;j>=oc;j--)
                {
                    dp[i][j] = max(dp[i][j],1+dp[i-zc][j-oc]);
                }
            }
        }
        return dp[m][n];
    }
};