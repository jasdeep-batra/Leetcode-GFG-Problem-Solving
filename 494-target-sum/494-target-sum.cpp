class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int target) {
        int sum =0;
        int size = nums.size();
        for(int i=0;i<size;i++)
        {
            sum+=nums[i];
        }
        if(sum < abs(target))return 0;
        if((sum+target)%2==1)return 0;
        int find = (sum+target)/2;
        cout<<sum<<":"<<find;
        vector<vector<int>> dp(size+1,vector<int>(find+1,0));        
        dp[0][0] = 1;
        for(int i=0;i<size+1;i++)
        {
            dp[i][0] = 1;
        }
        
        for(int i=1;i<size+1;i++)
        {
            for(int j=0;j<find+1;j++)
            {
              if(j >= nums[i-1])
              {
                  dp[i][j] = dp[i-1][j-nums[i-1]] + dp[i-1][j];
              }
              else{
                  dp[i][j] = dp[i-1][j];  
                }
            }
        }
        for(int i=0;i<nums.size()+1;i++)
        {
            for(int j=0;j<find+1;j++)
            {
                cout<<dp[i][j]<<" ";
            }
            cout<<endl;
        }
        int ans = dp[nums.size()][find];
        return ans;
    }
};