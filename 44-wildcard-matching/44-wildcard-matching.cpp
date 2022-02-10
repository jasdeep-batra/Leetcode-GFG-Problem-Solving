class Solution {
public:
    bool isMatch(string s, string p) {
        vector<vector<bool>> dp(p.size()+1,vector<bool>(s.size()+1,false));
        dp[0][0] = true;
        for(int i=1;i<p.size()+1;i++)
        {
            if(p[i-1]=='*')
            {
                dp[i][0] = dp[i-1][0];
            }
        }
        for(int i=1;i<p.size()+1;i++)
        {
            for(int j=1;j<s.size()+1;j++)
            {
                if(p[i-1]=='*')
                {
                    dp[i][j] = dp[i-1][j] || dp[i][j-1];
                }
                else
                {
                    if(s[j-1]==p[i-1] || p[i-1]=='?')
                    {
                        dp[i][j] = dp[i-1][j-1];                        
                    }
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