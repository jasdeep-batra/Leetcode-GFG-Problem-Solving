class Solution {
public:
    int numSubseq(vector<int>& nums, int target) {
        int min = 0;
        int max = nums.size()-1;
        long long cp = 0;
        int mod = 1000000007;
        sort(nums.begin(),nums.end());
        vector<int> count;
        count.push_back(1);
        for(int i=1;i<nums.size();i++)
        {
            count.push_back((count[i-1]*2)%mod);
        }
        while(max>=min)
        {
            if(nums[max]+nums[min] > target)
            {
                max--;
            }
            else
            {
                long long midele = (max-min)%mod;
                cp =(cp + count[max-min])%mod;
                min++;
            }
        }
        return cp%mod;
    }
};