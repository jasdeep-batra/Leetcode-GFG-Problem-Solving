class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int f = 0;
        int l = nums.size()-1;
        sort(nums.begin(),nums.end());
        while(f<l)
        {
            int m = f + (l-f)/2;
            if(nums[m]!=nums[m-1] && nums[m]!=nums[m+1])
            {
                return nums[m];
            }
            if((m-f+1)%2!=0)
            {                
                if(nums[m]==nums[m+1])
                {
                    f = m;
                }
                else
                {
                    l = m;
                }
            }
            else
            {
                if(nums[m]==nums[m-1])
                {
                    f = m+1;
                }
                else
                {
                    l = m-1;
                }
            }
        }
        return nums[f];
    }
};