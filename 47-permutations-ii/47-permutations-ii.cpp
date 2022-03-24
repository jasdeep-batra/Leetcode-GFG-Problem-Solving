class Solution {
public:
    set<vector<int>> result;
    int last;
   // void two_vec_equal()
    void recursion(vector<int>& num, list<int>& nums, int i, vector<int>& res)
    {
        if(nums.empty())
        {   
            cout<<"working";
            //for(auto itr: res)cout<<itr;
            cout<<endl;
            result.insert(res);
            return;
        }
        for(int j=0;j<nums.size();j++)
        {
           // if(i>0 && num[i]==num[i-1])continue;
            cout<<nums.front()<<endl;
            res.push_back(nums.front());
            int store = nums.front();
            nums.pop_front();
            recursion(num,nums,j+1,res);
            nums.push_back(store);
            res.pop_back();
        }
    }
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        vector<vector<int>> final_result;
        sort(nums.begin(),nums.end());
        list<int> lt;
        for(auto itr:nums)
        {
            lt.push_back(itr);
        }
        vector<int> res;
        recursion(nums,lt,0,res);
        for(auto itr: result)
        {
            final_result.push_back(itr);
        }
        return final_result;
    }
};