class Solution {
public:
    vector<vector<int>> result;
    void recur(vector<int> nums,int i, vector<int> row)
    {
        result.push_back(row);
        for(int j=i;j<nums.size();j++)
        {
            if(j!=i && nums[j]==nums[j-1]) continue;            
            row.push_back(nums[j]);
            recur(nums,j+1,row);
            row.pop_back();            
        }        
    }
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        //vector<vector<int>> result;
        sort(nums.begin(),nums.end());
        vector<int> row;        
        recur(nums,0,row);
        return result;
    }
};