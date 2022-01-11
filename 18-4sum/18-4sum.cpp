class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        sort(nums.begin(),nums.end());
        vector<vector<int>> result;
        if(nums.size()<4)
        {
            return result;
        }
        for(int i=0;i<nums.size()-3;i++)
        {
            int target3 = target - nums[i];
            if(i>0 && nums[i]==nums[i-1])
            {
                continue;
            }
            for(int j = i+1; j<nums.size();j++)
            {
                int target2 = target3 - nums[j];
                int p1 = j+1;
                int p2 = nums.size()-1;
                if(j>i+1 && nums[j]==nums[j-1])
                {
                    continue;
                }
                while(p2 > p1)
                {
                    if(nums[p1]+nums[p2]==target2)
                    {
                        while(p1<p2 && nums[p1]==nums[p1+1])
                        {
                            p1++;
                        }
                        while(p2>p1 && nums[p2]==nums[p2-1])
                        {
                            p2--;
                        }
                        vector<int> temp = {nums[i],nums[j],nums[p1],nums[p2]};
                        result.push_back(temp);
                        p1++;
                        p2--;
                    }
                    else if((nums[p1]+nums[p2])>target2)
                    {
                        p2--;
                    }
                    else if((nums[p1]+nums[p2])<target2)
                    {
                        p1++;
                    }
                }
            }
        }
        return result;
    }
};