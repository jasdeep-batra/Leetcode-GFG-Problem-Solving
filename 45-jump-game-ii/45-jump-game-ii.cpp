class Solution {
public:
    int jump(vector<int>& nums) {
        vector<int> dp(nums.size(),INT_MAX-1);
        dp[0] = 0;
        for(int i=1;i<nums.size();i++)
        {
            for(int j=0;j<i;j++)
            {
                if(j+nums[j] >= i)
                {
                    dp[i] = min(1+dp[j],dp[i]);                        
                }
            }
        } 
        for(int i=0;i<nums.size();i++)
        {
            cout<<dp[i]<<" ";
        }
        int ans = dp[dp.size()-1];
        return ans;
    }
};