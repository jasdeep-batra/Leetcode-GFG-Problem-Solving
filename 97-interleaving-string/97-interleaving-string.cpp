class Solution {
public:
    bool solve(int i, int j, int k, string& s1, string& s2, string& s3,vector<vector<int>>& dp)
        {
            if(i==0)
            {
                return s2.substr(0,j)==s3.substr(0,k);
            }
            if(j==0)
            {
                return s1.substr(0,i)==s3.substr(0,k);
            }
            if(dp[i][j]!=-1)return dp[i][j];
            if(s1[i-1]==s3[k-1] && s2[j-1]==s3[k-1])
            {
                return dp[i][j] = solve(i-1,j,k-1,s1,s2,s3,dp) || solve(i,j-1,k-1,s1,s2,s3,dp);
            }
            else if(s1[i-1]==s3[k-1])
            {
                return dp[i][j] = solve(i-1,j,k-1,s1,s2,s3,dp);
            }
            else if(s2[j-1]==s3[k-1])
            {
                return dp[i][j] = solve(i,j-1,k-1,s1,s2,s3,dp);
            }
            else return dp[i][j] = 0;
        }
    bool isInterleave(string s1, string s2, string s3) {
        if(s1.size()+s2.size()!=s3.size())return false;
        vector<vector<int>> dp(s1.size()+1,vector<int>(s2.size()+1,-1));
        return solve(s1.size(),s2.size(),s3.size(),s1,s2,s3,dp);
            
    }
};