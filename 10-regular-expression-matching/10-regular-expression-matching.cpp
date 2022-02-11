class Solution {
public:
    bool isMatch(string s, string p) {
        vector<vector<bool>> dp(p.size()+1,vector<bool>(s.size()+1,false));
        dp[0][0] = true;
        for(int i=1;i<p.size()+1;i++)
        {
            if(p[i-1]=='*')
            {
                dp[i][0] = dp[i-2][0];
            }
        }
        for(int i=1;i<p.size()+1;i++)
        {
            for(int j=1;j<s.size()+1;j++)
            {
                if(p[i-1]=='*')
                {
                    if(p[i-2]==s[j-1] || p[i-2]=='.')
                    {
                        dp[i][j] = dp[i-2][j] || dp[i][j-1];
                    }
                    else
                    {
                        dp[i][j] = dp[i-2][j];
                    }
                }
                else if(p[i-1]==s[j-1] || p[i-1]=='.')
                {
                    dp[i][j] = dp[i-1][j-1];
                }
            }
        }
        // for(int i=0;i<p.size()+1;i++)
        // {
        //     for(int j=0;j<s.size()+1;j++)
        //     {
        //         cout<<dp[i][j]<<" ";
        //     }
        //     cout<<endl;
        // }
        bool ans = dp[p.size()][s.size()];
        return ans;
    }
};