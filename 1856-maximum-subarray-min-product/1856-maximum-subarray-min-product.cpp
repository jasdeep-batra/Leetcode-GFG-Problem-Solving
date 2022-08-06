class Solution {
public:
    int maxSumMinProduct(vector<int>& nums) {
        vector<long long> sum(nums.size()+1,0);
        sum[0]=0;
        for(int i=1;i<nums.size()+1;i++)
        {
            sum[i] = sum[i-1]+nums[i-1];
        }
        vector<long long> nsl(nums.size(),0);
        vector<long long> nsr(nums.size(),0);
        stack<pair<long long,long long>> s;
        for(int i=0;i<nums.size();i++)
        {

            if(!s.empty() && s.top().first<nums[i])
            {
                nsl[i] = s.top().second;
                s.push({nums[i],i});
            }
            else{
                while(!s.empty() && (s.top().first>=nums[i]))
                {
                    s.pop();
                }
                if(!s.empty())
                {
                    nsl[i] = s.top().second;
                }
                else{
                    nsl[i]  = -1;
                }
                s.push({nums[i],i});
            }
        }
        while(!s.empty())s.pop();
        for(int i=nums.size()-1;i>=0;i--)
        {
            if(!s.empty() && nums[i]>s.top().first)
            {
                nsr[i] = s.top().second;
                s.push({nums[i],i});
            }
            else{
                while(!s.empty() && (s.top().first>=nums[i]))
                {
                    s.pop();
                }
                if(!s.empty())
                {
                    nsr[i] = s.top().second;
                }
                else{
                    nsr[i]  = nums.size();
                }
                s.push({nums[i],i});
            }
        }
        long long res = INT_MIN;
        for(int i=0;i<nums.size();i++)
        {
            //cout<<nums[i]*(sum[nsr[i]]-sum[nsl[i]+1])<<endl;
            long long diff = sum[nsr[i]]-sum[nsl[i]+1];
            long long as = nums[i]*diff;
            res = max(res,as);
        }
        // for(auto i:nsr)
        // {
        //     cout<<i<<" "; 
        // }
        // for(auto i:nsl)
        // {
        //     cout<<i<<" "; 
        // }
        return res%1000000007;
    }
};