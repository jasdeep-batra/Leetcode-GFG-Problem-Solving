class Solution {
public:
    // it is a problem of backtracking where you might have to use the for loop along in a recursive function./
    vector<vector<int>> result;
    void recursion(vector<int> num, int i, int k,vector<int> res)
    {
        if(k==0)
        {
            //for(auto itr: res)cout<<itr<<endl;
            result.push_back(res);
            return;
        }
        for(int it = i;it<num.size();it++)
        {
            int st = num[it];
            res.push_back(st);
            recursion(num,it+1,k-1,res);
            res.pop_back();            
        }
        
    }
    vector<vector<int>> combine(int n, int k) {
        vector<int> num;
        vector<int> res;
        for(int i=1;i<=n;i++)
        {
            num.push_back(i);
        }
        recursion(num,0,k,res);
        return result;
    }
};