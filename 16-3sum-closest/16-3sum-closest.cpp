class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        int ans = INT_MAX;
        sort(nums.begin(),nums.end());
        for(auto itr: nums)
        {
            cout<<itr<<" ";
        }
        map<int,int> mp;
        for(int i=0;i<nums.size()-2;i++)
        {   cout<<"i: "<<nums[i]<<endl;
            int j = i+1;
            int last = nums.size()-1;
            int nt = target - nums[i];
            if(i>0 && nums[i]==nums[i-1])continue;
            while(j<last)
            {                
                if(nums[j]+nums[last] <= nt)
                {
                    ans = nums[i] + nums[j] + nums[last];
                    cout<<"ans: "<<ans<<endl;
                    if(mp.find(abs(target-ans))!=mp.end())
                    {
                        if(mp[abs(target-ans)]>ans)
                            mp[abs(target-ans)] = ans;                        
                    } 
                    else{
                        mp[abs(target-ans)] = ans;
                    }
                    j++;
                }
                if(nums[j] + nums[last] > nt)
                {
                    ans = nums[i] + nums[j] + nums[last];
                    cout<<"ans: "<<ans<<endl;
                    if(mp.find(abs(target-ans))!=mp.end())
                    {
                        if(mp[abs(target-ans)] > ans)
                            mp[abs(target-ans)] = ans;                        
                    } 
                    else{
                        mp[abs(target-ans)] = ans;
                    }
                    last--;
                }                              
            }
        }
        ans = mp.begin()->second;
        return ans;
    }
};