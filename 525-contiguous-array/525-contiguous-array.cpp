class Solution {
public:
    int findMaxLength(vector<int>& nums) {
        //which data structure can we use
        //it's brute force is simple
        // vector<pair<int,pair<int,int>>> vt;
        // int cnt0 = 0, cnt1 = 0,len = 1;
        // if(nums[i]==0)cnt0++;
        // else cnt1++;
        // for(int i=1;i<nums.size();i++)
        // {
        //     if(nums[i]==0)cnt0++;
        //     else cnt1++;
        //     len++;
        //     vt.push_back({len,{cnt0,cnt1}});
        //     if(cnt0==cnt1){
        //         ans = max(ans,len);
        //     }
        // }
        unordered_map<int,int> mp;
        int max_len = 0;
        int sum  = 0;
        mp[0] = -1;
        for(int i=0;i<nums.size();i++)
        {
            (nums[i]==1)?sum++:sum--;
            if(mp.find(sum)!=mp.end()){
                max_len = max(max_len,i-mp[sum]);
            }
            else{
                mp[sum] = i;
            }
        }
        return max_len;
    }
};