class Solution {
public:
    int wiggleMaxLength(vector<int>& nums) {
        int p = 1;
        int n = 1;
        for(int i=1;i<nums.size();i++)
        {
            if(nums[i]>nums[i-1]) p = n+1;
            if(nums[i]<nums[i-1])n = p+1;
        }
        return max(p,n);
    }
};