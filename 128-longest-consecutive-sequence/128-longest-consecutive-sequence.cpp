class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        //brute force method
        if(nums.size()==0)return 0;
        if(nums.size()==1)return 1;
        sort(nums.begin(),nums.end());
        int count=1,result=0;
        for(int i=1;i<nums.size();i++)
        {
            if(nums[i]==nums[i-1]+1)
            {
                count++;
            }
            else if(nums[i]==nums[i-1])
            {
                continue;
            }
            else
            {
                result = max(result,count);
                count = 1;
            }
        }
        result = max(result, count);
        return result;
    }
};