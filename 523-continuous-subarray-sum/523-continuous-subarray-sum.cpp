class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k) {
        unordered_map<int,int> mp;
        int prefix = 0;
        mp[0] = -1;
        for(int i=0;i<nums.size();i++)
        {
            prefix+=nums[i];
            prefix%=k;
            if(prefix==0 && i)return true;
            if(mp.find(prefix)!=mp.end())
            {
                if(i-mp[prefix]>1)return true;
            }
            else mp[prefix] = i;
        }
        return false;
    }
};