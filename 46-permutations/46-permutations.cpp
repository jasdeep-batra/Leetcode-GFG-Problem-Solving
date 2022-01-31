class Solution {
public:
    vector<vector<int>> result;
    void recursion(list<int> nums, vector<int> res)
    {
        if(nums.size()==0){
            result.push_back(res);
            return;
        }
        for(int i=0;i<nums.size();i++)
        {
            int f = nums.front();
            res.push_back(f);
            nums.pop_front();
            recursion(nums,res);
            nums.push_back(f);
            res.pop_back();
        }
    }
    vector<vector<int>> permute(vector<int>& nums) {
        list<int> lt;
        for(auto itr: nums)
        {
            lt.push_back(itr);
        }
        vector<int> res;
        recursion(lt,res);
        return result;
    }
};