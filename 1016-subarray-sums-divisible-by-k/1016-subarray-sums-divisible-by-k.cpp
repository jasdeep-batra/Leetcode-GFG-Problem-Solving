class Solution {
public:
    int subarraysDivByK(vector<int>& nums, int k) {
        int count = 0;
        int prefix = 0;
        unordered_map<int,int> mp;
        mp[0] =   1;
        for(auto i: nums)
        {
            prefix+=i;
            int mod = prefix%k;
            if(mod < 0)
            {
                mod+=k;
            }
            if(mp.count(mod))
            {
                count+=mp[mod];
                mp[mod]+=1;
            }
            else{
                mp[mod] = 1;
            }
        }
        return count;
    }
};