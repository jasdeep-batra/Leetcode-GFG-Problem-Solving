class Solution {
public:
    vector<vector<string>> result;
    bool ispalin(string s, int first, int last)    
    {
        while(first<=last)
        {
            if(s[first]!=s[last])
            {
                return false;
            }
            first++;
            last--;
        }
        return true;
    }
    void recur(string s, int index, vector<string> res)
    {
        //base condition;
        if(index==s.size())
        {
            result.push_back(res);
            return;
        }
        for(int i = index;i<s.size();i++)
        {
            if(ispalin(s,index,i))
            {
                res.push_back(s.substr(index,i-index+1));
                recur(s,i+1,res);
                res.pop_back();
            }
        }
    }
    vector<vector<string>> partition(string s) {
        vector<string> res;
        recur(s,0,res);
        return result;
    }
};