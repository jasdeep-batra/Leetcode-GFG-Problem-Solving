class Solution {
public:
    int K;
    bool backtracking(vector<int>& nums, vector<bool>& visit, int req_sum,int sum, int i,int bucket_size)
    {
        if(bucket_size==1)return true;
        if(sum == req_sum)
        {
            return backtracking(nums,visit,req_sum,0,K - bucket_size + 1,bucket_size-1);
        }
        for(int ind=i;ind<nums.size();ind++)
        {
            if(nums[ind]!=0 && sum+nums[ind]<=req_sum)
            {
                int tem = nums[ind];
                nums[ind] = 0;
                if(backtracking(nums,visit,req_sum,sum+tem,ind+1,bucket_size))
                {
                    return true;
                }
                nums[ind] = tem;
            }
        }
        return false;
    }
    bool canPartitionKSubsets(vector<int>& nums, int k) {
        int sum =0;
        K= k;
        for(int i=0;i<nums.size();i++)sum+=nums[i];
        if(sum%k!=0)return false;
        //Now we will write one function
        int req_sum = sum/k;
        sort(nums.begin(),nums.end());
        vector<bool> visit(nums.size(),false);
        return backtracking(nums,visit,req_sum,0,0,k);
        
    }
};