class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int i=0,j=nums.size()-1;
        int product_suffix = 1;
        vector<int> arr(nums.size(),1);
        for(int k=1;k<nums.size();k++)
        {
            arr[k] = arr[k-1]*nums[k-1];
        }
        int product_prefix = 1;
        while(j>=0)
        {
            arr[j] = arr[j]*product_suffix;
            product_suffix *= nums[j];
            j--;
        }
        //nums[i] = product_suffix*product_prefix;
        return arr;
    }
};