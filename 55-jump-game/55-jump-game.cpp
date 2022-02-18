class Solution {
public:
    bool canJump(vector<int>& nums) {
        int limit = 0;
        for(int i=0;i<nums.size();i++)
        {
            if(i>limit)
            {
                return false;
            }
            if(limit >= nums.size()-1)
            {
                return true;
            }
            else
            {
                limit = max(limit,i+nums[i]);
            }
        }
        if(limit>=nums.size()-1)return true;
        return false;
    }
};