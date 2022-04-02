class Solution {
public:
    vector<vector<int>> result;
    void recursion(vector<int> candid, int target, int size, vector<int> res)
    {
        if(target==0){result.push_back(res);return;}
        if(size==0)
        {
            return;
        }
        if(target>=candid[size-1])
        {
            res.push_back(candid[size-1]);
            recursion(candid,target-candid[size-1],size,res);
            res.pop_back();
        }
        recursion(candid,target,size-1,res);
    }
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        //here we have two choices 
        //1.) either we can use multiple same numbers 
        //2.) or we won't include it.
        //in backtracking we not necessarily need to use additional for loop 
        vector<int>res;
        recursion(candidates,target,candidates.size(),res);
        return result;
    }
};