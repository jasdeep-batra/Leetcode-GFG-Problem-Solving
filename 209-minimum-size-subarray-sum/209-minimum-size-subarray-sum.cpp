class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        //sort(nums.begin(),nums.end());
        int i=0;
        int j=0;
        int sum =0;
        int len = INT_MAX;
        while(i<nums.size())  // 1 2 2 3 3 4
        {
            if(i>j)break;
            
            if(j<nums.size() && sum<target){
                sum+=nums[j];
                j++;
            }
            else
            {
                if(sum>=target)len = min(len,j-i);
                sum-=nums[i];
                i++;
            }
        }
        if(len==INT_MAX)return 0;
        return len;
    }
};