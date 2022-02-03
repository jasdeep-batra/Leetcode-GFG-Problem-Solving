class Solution {
public:
    vector<vector<int>> result;
    void recursion(vector<int> nums, int n, vector<int> res)
    {
        if(n==0)
        {
            result.push_back(res);
            return;
        }
        res.push_back(nums[n-1]);
        recursion(nums, n-1, res);
        res.pop_back();
        recursion(nums,n-1,res);
            
    }
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<int> res;
        recursion(nums,nums.size(),res);
        return result;
    }
};