class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        if(nums.size()==1)return (nums[0]==1)? 1:0;
        
        int i=0;
        int j =0;
        int res = 0;
        while(j<nums.size())
        {
            if(nums[i]==1 && nums[i]==nums[j])
            {
                j++;
            }
            else if(nums[i]==0)
            {
                i++;
                j=i;
            }
            else{
                res = max(res,j-i);
                i = j+1;
                j = i;
            }
        }
        res = max(res,j-i);
        return res;
    }
};