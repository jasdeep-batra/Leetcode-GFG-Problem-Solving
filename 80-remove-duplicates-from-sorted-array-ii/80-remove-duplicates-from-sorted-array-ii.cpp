class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int n=nums.size();
        int i,k=1;
        int count=1,ans=0;
        for(i=1;i<n;i++)
        {
            if(nums[i]==nums[i-1])
            {
                count++;
                if(count>2)
                    ans++;
                else
                    nums[k++]=nums[i];
            }
            else
            {
                nums[k++]=nums[i];
                count=1;
            }
        }
        
        return n-ans;
    }
};