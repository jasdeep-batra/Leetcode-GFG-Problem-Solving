class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        map<string,int> mp;
        for(int i=0;i<wordDict.size();i++)
        {
            mp[wordDict[i]] = 1;
        }
        vector<vector<bool>> dp(s.size(),vector<bool>(s.size(),0));
        for(int i=0;i<s.size();i++)  //a size of a sliding window
        {
            for(int j=0;j+i<s.size();j++)
            {
                string ch = s.substr(j,i+1);
                if(mp.find(ch)!=mp.end())
                {
                    dp[j][j+i] = 1;
                }
                else
                {
                    bool flag = false;
                    for(int k=j;k<j+i;k++)
                    {
                        if(dp[j][k] && dp[k+1][j+i])
                        {
                            flag = true;
                            break;
                        }
                    }
                    dp[j][j+i] = flag;
                }
            }
        }
        return dp[0][s.size()-1];        
    }
};