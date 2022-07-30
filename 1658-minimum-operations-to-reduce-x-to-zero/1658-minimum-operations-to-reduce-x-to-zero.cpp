class Solution {
public:
    int minOperations(vector<int>& nums, int x) {
        int sum = 0;
        for(auto i: nums)sum+=i;
        int k = sum-x;
        int i=0,j=0,sumw = 0,res=INT_MIN;bool found = false;
        while(j<nums.size())
        {
            sumw+=nums[j];
            while(i<=j && sumw>k){
                sumw-=nums[i];
                i++;    
                }
            if(sumw==k){
                found = true;
                res = max(res,j-i+1);
            }
                j++;
            
        }
        return found? nums.size()-res:-1;
    }
};