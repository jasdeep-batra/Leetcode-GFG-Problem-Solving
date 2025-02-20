class Solution {
public:
    void helper(int n, string s, string& res,vector<string>& nums)
    {
        if (s.size()==n){
            if(find(nums.begin(),nums.end(),s)==nums.end()){
                res = s;
            }
            return;
        }
        for(int i=0;i<=1;i++){
            helper(n,s+(char)(i+'0'),res,nums);
        }
        return;
    }
    string findDifferentBinaryString(vector<string>& nums) {
        // of n lenght how many unique can be build?
        string res = "";
        int n  = nums[0].size();
        helper(n,"",res,nums);
        return res;
    }
};