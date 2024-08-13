class Solution {
public:
    vector<vector<int>> result;
    void recur(vector<int> arr, int target, int n, vector<int> row) //7
    {
        if(target==0)
        {  
            result.push_back(row);
         return;
        }
        for(int i = n;i<arr.size();i++)
        {
            if(i>n && arr[i]==arr[i-1])continue;
            
            if(target<arr[i]) break;
            
            row.push_back(arr[i]);
            recur(arr,target-arr[i],i+1,row);
            row.pop_back();           
        }
        
    }
    vector<vector<int>> combinationSum2(vector<int>& arr, int target) {
        sort(arr.begin(),arr.end());
        vector<int> row;
        recur(arr,target,0,row);
        return result;
    }
};