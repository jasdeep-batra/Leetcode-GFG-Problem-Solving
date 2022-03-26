class Solution {
public:
    int search(vector<int>& nums, int target) {
        //modifyed binary search
        int first = 0;
        int last = nums.size()-1;
        while(last>=first)
        {
            int mid = (last+first)/2;
            if(nums[mid]==target)
            {
                return mid;
            }
            if(nums[first]<=nums[mid])
            {
                if(target>=nums[first] && target<nums[mid])
                {
                    last = mid-1;
                }
                else
                {
                    first = mid+1;
                }
            }
            else
            {
                if(target>nums[mid] && target<=nums[last])
                {
                    first = mid+1;
                }
                else
                {
                    last = mid-1;
                }
            }
        }
        return -1;
    }
};