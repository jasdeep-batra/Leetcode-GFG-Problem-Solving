class Solution {
public:
    long long zeroFilledSubarray(vector<int>& nums) {
        vector<long long> res;
        int i=-1,j=0;
        while(j<nums.size())
        {
            if(nums[j]!=0){
                if(j!=i+1)res.push_back((j-i-1));
                i = j;                
            }
            j++;
        }
        //if(j==nums.size()-1 && nums[j]!=0)res.push_back(j-i-1);
        if(nums[nums.size()-1]==0)res.push_back(j-i-1);
        long long count = 0;
        for(auto k: res)
        {
            long long a = (k*(k+1))/2;
            count+=a;
        }
        return count;
        
    }
};