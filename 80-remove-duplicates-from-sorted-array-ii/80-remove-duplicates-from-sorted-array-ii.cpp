class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int i=0,j=1;
        while(j<nums.size())
        {
            if(nums[i]==nums[j])j++;
            // else if(j-i+1>2)
            // {
            //     nums.erase(nums.begin()+j);
            // }
            else if(j-i<=2)
            {
                i=j;
                j++;
            }
            else if(j-i>2)
            {
                nums.erase(nums.begin()+j-1);
                j--;
            }
        }
        // for(auto itr:nums)
        // {
        //     cout<<itr<<" ";
        // }
        while(j-i>2)
        {
            nums.erase(nums.begin()+j-1);
            j--;
        }
        return nums.size();
    }
};