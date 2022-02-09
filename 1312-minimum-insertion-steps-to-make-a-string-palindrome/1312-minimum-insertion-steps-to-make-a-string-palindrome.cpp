class Solution {
public:
    int minInsertions(string s) {
        string rs = s;
        reverse(rs.begin(),rs.end());
        vector<vector<int>> dp(s.size()+1,vector<int>(s.size()+1,0));
        for(int i=1;i<s.size()+1;i++)
        {
            for(int j=1;j<s.size()+1;j++)
            {
                if(s[i-1]==rs[j-1])
                {
                    dp[i][j] = 1+dp[i-1][j-1];
                }
                else
                {
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1]);
                }
            }            
        }
        int ans = dp[s.size()][s.size()];
        int res = s.size()-ans;
        return res;
    }
};