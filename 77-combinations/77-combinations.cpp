class Solution {
public:
    // it is a problem of backtracking where you might have to use the for loop along in a recursive function./
    vector<vector<int>> result;
    void recursion(int i, int k,vector<int>&current,int n)
    {
        if(current.size()==k)
        {
           // for(auto itr: res)cout<<itr<<" ";
            
            result.push_back(current);
            return;
        }
        for(int j=i;j<n+1;j++)
        {
            current.push_back(j);
             recursion(j+1,k,current,n);
            current.pop_back();            
        }
        
    }
    vector<vector<int>> combine(int n, int k) {
        vector<int> res;
         recursion(1,k,res,n);
        return result;
    }
};