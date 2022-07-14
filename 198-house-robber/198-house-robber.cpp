class Solution {
public:
    int res;
    vector<int> dp;
    int solve(vector<int>& nums, int i, int collect)
    {
        //base condition
        if(i>=nums.size())
        {
            return 0;
        }
        if(dp[i]!=-1)return dp[i];
            
            return dp[i] = max(solve(nums,i+1,collect),nums[i]+solve(nums,i+2,collect));
        
        
    }
    int rob(vector<int>& nums) {
        dp.resize(nums.size(),-1);
        res  = 0;
        int collect = 0;
        return solve(nums,0,collect);
    }
};