class Solution {
public:
    string longestPalindrome(string s) {
        if(s.size()<=1)return s;
        string ans=s.substr(0,1);
        vector<vector<int>> dp(s.size(),vector<int>(s.size(),0));
        for(int i=1;i<s.size();i++)
        {
            dp[i-1][i-1] = 1;
            if(s[i-1] == s[i])dp[i-1][i] = 1;
            if(dp[i-1][i]==1)
            {
                if(ans.size()<2)ans = s.substr(i-1,2);
            }
        }
        for(int i=2;i<s.size();i++)
        {
            for(int j = 0;j+i<s.size();j++)
            {
                if(s[j+i]==s[j] && dp[j+1][j+i-1]==1)
                {
                    dp[j][j+i] = 1;
                }
                if(dp[j][j+i]==1)
                {
                    if(ans.size()<(i+1))
                    ans = s.substr(j,i+1);
                }
            }
        }
        
        // for(int i=0;i<s.size();i++)
        // {
        //     for(int j = 0;j<s.size();j++)
        //     {
        //         if(dp[i][j]==1)
        //         {
        //             if(ans.size()<(j-i+1))
        //             ans = s.substr(i,j-i+1);
        //         }
        //     }            
        // }
        return ans;
    }
};