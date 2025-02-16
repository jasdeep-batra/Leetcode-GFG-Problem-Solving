class Solution {
public:
    vector<vector<int>> memo;
    bool helper(vector<int>& nums,int i,int target)
    {
        if (target==0) return true;
        if (i>=nums.size() || target<0)
        {
            return false;
        }
        if(memo[i][target]!=-1){
            return memo[i][target];
        }
        return memo[i][target] = helper(nums,i+1,target-nums[i]) || helper(nums,i+1,target);
    }
    bool canPartition(vector<int>& nums) {
        
        int sum = 0;
        for(auto i: nums)
        {
            sum+=i;
        }
        if(sum%2!=0)return false;
        int target = sum/2;
        memo.resize(nums.size(),vector<int>(target+1,-1));
        return helper(nums,0,target);
    }
};