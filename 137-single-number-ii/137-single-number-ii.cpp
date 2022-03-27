class Solution {
public:
    int singleNumber(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        map<int,int> mp;
        int count = 1;
        for(int i=0;i<nums.size();i++)
        {
            mp[nums[i]]++;            
        }
        for(auto itr:mp)
        {
            if(itr.second==1)
                return itr.first;
        }
        return -1;
        
    }
};