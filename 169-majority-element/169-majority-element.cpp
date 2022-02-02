class Solution {
public:
    int majorityElement(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int i=0,j=0,count = 0;
        while(j<nums.size())
        {
            if(nums[i]==nums[j])
            {
                count++;
                j++;
            }
            else
            {
                if(count > (nums.size()/2))return nums[i];
                i = j;
                count = 0;
            }
        }
        return nums[i];
    }
};