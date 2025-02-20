class Solution {
public:
    bool helper(int n, string s, string& res,vector<string>& nums)
    {
        if (s.size()==n){
            if(find(nums.begin(),nums.end(),s)==nums.end()){
                res = s;
                return true;
            }
            return false;
        }
        for(int i=0;i<=1;i++){
            if(helper(n,s+(char)(i+'0'),res,nums))
            {
                return true;
            }
        }
        return false;
    }
    string findDifferentBinaryString(vector<string>& nums) {
        // of n lenght how many unique can be build?
        string res = "";
        int n  = nums[0].size();
        bool ans = helper(n,"",res,nums);
        return res;
    }
};