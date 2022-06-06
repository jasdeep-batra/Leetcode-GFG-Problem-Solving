class Solution {
public:
    bool is_triangle(int i, int j, int k)
    {
        if(i+j>k && j+k>i && i+k>j)return true;
        return false;
    }
    int triangleNumber(vector<int>& nums) {
        int ans = 0;
        sort(nums.begin(),nums.end());
        for(int i=nums.size()-1;i>1;i--)
        {
            int j = i-1;
            int k = 0;
            while(k<j)
            {
                if((nums[j]+nums[k])>nums[i])
                {
                    ans+=(j-k);
                    j--;
                }
                else{
                    k++;                    
                }
            }   
        }            
        return ans;
    }
};