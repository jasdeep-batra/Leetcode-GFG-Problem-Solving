class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {
        if(nums.size()==1)return nums[0];
        int first = 0;
        int last = nums.size()-1;
        int mid = 0;
        while(last >= first)
        {
            mid = (last+first)/2;
            int n = 0;
            if((mid+1)%2==0){
                n = mid-1;
            }
            else{
                n = mid+1;
            }
            if(nums[mid]==nums[n])first = mid+1;
            else if((mid>0 && mid<nums.size()-1) && (nums[mid]!=nums[mid-1] && nums[mid]!=nums[mid+1])) return nums[mid];
            else last = mid-1;
        } 
        return nums[mid];
    }
};