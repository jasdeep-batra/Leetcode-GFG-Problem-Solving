class Solution {
public:
    int findLength(vector<int>& nums1, vector<int>& nums2) {
        int s1 = nums1.size();
        int s2 = nums2.size();
        vector<vector<int>>dp(s1+1,vector<int> (s2+1,0));
        for(int i=1;i<s1+1;i++)
        {
            for(int j=1;j<s2+1;j++)
            {
                if(nums1[i-1]==nums2[j-1])
                {
                    dp[i][j] = 1 + dp[i-1][j-1];
                }
                else
                {
                    dp[i][j] = 0;
                }
            }
        }
        int ans = 0;
        for(int i=0;i<s1+1;i++)
        {
            for(int j=0;j<s2+1;j++)
            {
                ans = max(ans,dp[i][j]);
            }
        }
        
        return ans;
    }
};